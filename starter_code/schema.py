from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn:
    document_id, source_type, author, category, content, timestamp.
    """

    document_id: str = Field(..., description="Unique ID của tài liệu")
    source_type: str = Field(..., description="Nguồn dữ liệu (pdf, video, etc.)")
    author: str = Field(..., description="Tác giả hoặc người tạo nội dung")
    category: str = Field(..., description="Phân loại nội dung")
    content: str = Field(..., description="Nội dung chính của tài liệu")
    timestamp: str = Field(..., description="Thời điểm tạo hoặc thu thập dữ liệu")