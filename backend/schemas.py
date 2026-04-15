from marshmallow import Schema, fields

class WorkoutSchema(Schema):
    id = fields.Int()
    exercise = fields.Str()
    duration = fields.Int()
    calories = fields.Int()

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)