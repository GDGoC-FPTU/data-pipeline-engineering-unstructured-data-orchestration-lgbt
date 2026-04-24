import re

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================

def process_pdf_data(raw_json: dict) -> dict:
    # Bước 1: Làm sạch nhiễu (Header/Footer) khỏi văn bản
    raw_text = raw_json.get("extractedText", "")
    # Xóa mọi biến thể HEADER_PAGE_<số> và FOOTER_PAGE_<số> xuất hiện trong nội dung.
    cleaned_content = re.sub(r"\b(?:HEADER|FOOTER)_PAGE_\d+\b", "", raw_text)
    cleaned_content = re.sub(r"\s+", " ", cleaned_content).strip()
    
    # Bước 2: Map dữ liệu thô sang định dạng chuẩn của UnifiedDocument
    # Trả về dictionary với các key: document_id, source_type, author, category, content, timestamp
    return {
        "document_id": str(raw_json.get("docId", "")),
        "source_type": "PDF",
        "author": str(raw_json.get("authorName", "unknown")).strip() or "unknown",
        "category": str(raw_json.get("docCategory", "Uncategorized")).strip() or "Uncategorized",
        "content": cleaned_content,
        "timestamp": str(raw_json.get("createdAt", "")),
    }

def process_video_data(raw_json: dict) -> dict:
    # Map dữ liệu thô từ Video sang định dạng chuẩn (giống PDF)
    # Lưu ý các key của Video: video_id, creator_name, transcript, category, published_timestamp
    return {
        "document_id": str(raw_json.get("video_id", "")),
        "source_type": "Video",
        "author": str(raw_json.get("creator_name", "unknown")).strip() or "unknown",
        "category": str(raw_json.get("category", "Uncategorized")).strip() or "Uncategorized",
        "content": str(raw_json.get("transcript", "")).strip(),
        "timestamp": str(raw_json.get("published_timestamp", "")),
    }
