import wtforms
from wtforms.validators import Length, InputRequired
from models import UserModel, ParameterDataModel, ThermochemistryDataModel, DatabaseModel
from exts import db


# compound_new_data_.html中选择database验证
class DatabaseSelectedForm(wtforms.Form):
    # 验证database名称合规
    database_name = wtforms.StringField(validators=[Length(min=1, max=50, message="数据库名称格式错误")])
    # 提交表单数据
    belonging = wtforms.SelectField('belonging', choices=[
        ('USERDATA', 'USERDATA'),
        ('BINSBASE', 'BINSBASE'),
        ('ELEMBASE  ', 'ELEMBASE'),
        ('FACT53BASE  ', 'FACT53BASE'),
        ('FACTBASE', 'FACTBASE'),
        ('FScoppBASE', 'FScoppBASE'),
        ('FSleadBASE', 'FSleadBASE'),
        ('FSliteBASE', 'FSliteBASE'),
        ('FSnoblBASE', 'FSnoblBASE'),
        ('FSstelBASE', 'FSstelBASE'),
        ('FSupsiBASE', 'FSupsiBASE'),
        ('FThallBASE', 'FThallBASE'),
        ('FThelgBASE', 'FThelgBASE'),
        ('FTliBASE', 'FTliBASE'),
        ('FTliteBASE', 'FTliteBASE'),
        ('FTmiscBASE', 'FTmiscBASE'),
        ('FToxidBASE', 'FToxidBASE'),
        ('FTpulpBASE', 'FTpulpBASE'),
        ('FTsaltBASE', 'FTsaltBASE'),
    ])

    def validate_name(self, field):
        database_name = field.data
        name = DatabaseModel.query.filter_by(database_name=database_name).first()
        if name:
            raise wtforms.ValidationError(message="该名称已存在！")
