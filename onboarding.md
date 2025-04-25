# Code Review Checklist for Junior Developers

## 1. API Endpoint Design & Documentation
- Make sure endpoint names RESTful and meaningful
- Make sure HTTP methods correctly used
- Make sure status codes appropriate and consistent
- Make sure error messages clear and user-friendly

## 2. Database Query Optimization
- Are you using `.select_related()` or `.prefetch_related()` for related models?
- Are there any unintentional `N+1` queries?
- Avoid unnecessary `.all()` calls in views or serializers — use filtering when needed.
- Are any loops doing DB queries that could be refactored to bulk operations?

## 3. Django Best Practices
- Are class-based views used appropriately (e.g., `ModelViewSet` for CRUD)?
- Is `get_queryset()` used for queryset filtering based on user or context?
- Are business logic and view logic separated (e.g., use services/tasks for processing)?
- Are third-party packages properly configured and used only when needed?
- Are permissions (`IsAuthenticated`, custom permission classes) clearly applied?
- Are serializers validating data properly (`validate_<field>` or `validate()` methods)?

# 🚀 Simple Onboarding Plan for Junior Devs

## 🗓️ Week 1: Foundations
- Access setup
- Walkthrough of codebase
- Environment setup with `README.md` + `docker-compose` if used
- Intro to project goals

## 🗓️ Week 2: First Contributions
- Write basic functionality and an easy task

## 🗓️ Week 3–4: Independent Tasks
- Small bug fixes
- Create their first PR