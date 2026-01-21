# backend/src/db/models.py

from sqlalchemy import Column, String, Integer, Text, TIMESTAMP, JSON, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

from src.db.base import Base


class Candidate(Base):
    """
    Stores candidate information and uploaded resumes
    """
    __tablename__ = "candidates"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(50), nullable=True)
    resume_url = Column(Text, nullable=True)
    resume_text = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    profile = relationship("CandidateProfile", back_populates="candidate", uselist=False)
    questions = relationship("Question", back_populates="candidate")


class CandidateProfile(Base):
    """
    Parsed and analyzed candidate profile data
    """
    __tablename__ = "candidate_profiles"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    candidate_id = Column(UUID(as_uuid=True), ForeignKey("candidates.id", ondelete="CASCADE"))
    
    # Extracted information (stored as JSON)
    skills = Column(JSON, nullable=True)  # ["Python", "React", "AWS"]
    experience_years = Column(Integer, nullable=True)
    education = Column(JSON, nullable=True)  # [{"degree": "BS", "field": "CS"}]
    work_history = Column(JSON, nullable=True)  # [{"company": "Google", "role": "SWE"}]
    domain_expertise = Column(JSON, nullable=True)  # ["fintech", "e-commerce"]
    
    # AI analysis
    seniority_level = Column(String(50), nullable=True)  # junior/mid/senior
    strengths = Column(ARRAY(Text), nullable=True)
    knowledge_gaps = Column(ARRAY(Text), nullable=True)
    
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    
    # Relationships
    candidate = relationship("Candidate", back_populates="profile")


class Question(Base):
    """
    Generated interview questions
    """
    __tablename__ = "questions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    candidate_id = Column(UUID(as_uuid=True), ForeignKey("candidates.id"), nullable=True)
    
    # Question content
    title = Column(String(500), nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(String(20), nullable=False)  # easy/medium/hard
    category = Column(String(50), nullable=False)  # algorithms/system-design/debugging
    
    # Test cases and solution
    test_cases = Column(JSON, nullable=True)
    solution_code = Column(Text, nullable=True)
    solution_explanation = Column(Text, nullable=True)
    
    # Follow-up questions
    follow_ups = Column(JSON, nullable=True)
    
    # Metadata
    estimated_time = Column(Integer, nullable=True)  # minutes
    tags = Column(ARRAY(Text), nullable=True)
    personalization_context = Column(Text, nullable=True)
    
    # AI generation metadata
    generation_prompt = Column(Text, nullable=True)
    llm_model = Column(String(50), nullable=True)
    generation_cost = Column(Float, nullable=True)
    
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    
    # Relationships
    candidate = relationship("Candidate", back_populates="questions")