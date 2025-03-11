from flask import Blueprint, request, jsonify
from models import db, AttendanceLog
from datetime import datetime

api_bp = Blueprint('api', __name__)

# Get all attendance logs
@api_bp.route('/attendance', methods=['GET'])
def get_attendance():
    logs = AttendanceLog.query.all()
    return jsonify([{
        'id': log.id,
        'student_id': log.student_id,
        'course_id': log.course_id,
        'date': log.date.strftime('%Y-%m-%d'),
        'status': 'Present' if log.status else 'Absent'
    } for log in logs])

# Add new attendance log
@api_bp.route('/attendance', methods=['POST'])
def add_attendance():
    data = request.get_json()
    new_log = AttendanceLog(
        student_id=data['student_id'],
        course_id=data['course_id'],
        date=datetime.strptime(data['date'], '%Y-%m-%d'),
        status=data['status']
    )
    db.session.add(new_log)
    db.session.commit()
    return jsonify({'message': 'Attendance added successfully'}), 201

# Update attendance log
@api_bp.route('/attendance/<int:id>', methods=['PUT'])
def update_attendance(id):
    log = AttendanceLog.query.get(id)
    if not log:
        return jsonify({'message': 'Log not found'}), 404
    data = request.get_json()
    log.status = data.get('status', log.status)
    db.session.commit()
    return jsonify({'message': 'Attendance updated successfully'})

# Delete attendance log
@api_bp.route('/attendance/<int:id>', methods=['DELETE'])
def delete_attendance(id):
    log = AttendanceLog.query.get(id)
    if not log:
        return jsonify({'message': 'Log not found'}), 404
    db.session.delete(log)
    db.session.commit()
    return jsonify({'message': 'Attendance deleted successfully'})
