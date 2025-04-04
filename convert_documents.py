import os
import json
from pathlib import Path
import math

def split_text_into_chunks(text, chunk_size=900000):  # ~900KB chunks to stay under 1MB limit
    """Split text into chunks of approximately equal size."""
    words = text.split()
    chunk_size_words = math.ceil(len(words) / math.ceil(len(text) / chunk_size))
    
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        current_chunk.append(word)
        current_size += len(word) + 1  # +1 for space
        
        if current_size >= chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_size = 0
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def convert_documents_to_jsonl():
    # Path to the documents directory
    documents_dir = Path("documents")
    
    # Output directory for JSONL files
    output_dir = Path("langsmith_datasets")
    output_dir.mkdir(exist_ok=True)
    
    # Get all .txt files
    txt_files = list(documents_dir.glob("*.txt"))
    
    # Process files in batches
    batch_size = 100  # Number of documents per JSONL file
    current_batch = []
    batch_number = 1
    
    for txt_file in txt_files:
        try:
            # Read the content of each file
            with open(txt_file, 'r', encoding='utf-8') as doc:
                content = doc.read()
            
            # Split content into chunks if needed
            chunks = split_text_into_chunks(content)
            
            # Create JSON objects for each chunk
            for chunk_idx, chunk_content in enumerate(chunks):
                metadata = {
                    "filename": txt_file.name,
                    "size": len(chunk_content),
                    "chunk_index": chunk_idx,
                    "total_chunks": len(chunks),
                    "original_size": os.path.getsize(txt_file),
                    "document_id": txt_file.stem
                }
                
                # Format according to LangSmith requirements
                doc_json = {
                    "inputs": {
                        "content": chunk_content,
                        "metadata": metadata
                    },
                    "outputs": {
                        "document_id": f"{txt_file.stem}_chunk_{chunk_idx}"
                    }
                }
                current_batch.append(doc_json)
            
            # Write batch to file when it reaches the batch size
            if len(current_batch) >= batch_size:
                output_file = output_dir / f"documents_batch_{batch_number}.jsonl"
                with open(output_file, 'w', encoding='utf-8') as f:
                    for doc in current_batch:
                        f.write(json.dumps(doc) + '\n')
                print(f"Created batch {batch_number} with {len(current_batch)} chunks")
                current_batch = []
                batch_number += 1
                
        except Exception as e:
            print(f"Error processing {txt_file}: {str(e)}")
    
    # Write any remaining documents in the last batch
    if current_batch:
        output_file = output_dir / f"documents_batch_{batch_number}.jsonl"
        with open(output_file, 'w', encoding='utf-8') as f:
            for doc in current_batch:
                f.write(json.dumps(doc) + '\n')
        print(f"Created final batch {batch_number} with {len(current_batch)} chunks")
    
    print(f"Conversion complete. Created {batch_number} batch files in {output_dir}")
    print(f"Processed {len(txt_files)} files")

if __name__ == "__main__":
    convert_documents_to_jsonl() 