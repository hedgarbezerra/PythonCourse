import re
import datetime


class Validate:

    @staticmethod
    def email_is_valid(email):
        """Essa Regex irá aceitar todos tipos de char definidos pelo ^@ porém deve existir um @ e pelo menos um . após o mesmo"""
        EMAIL_REGEX = re.compile('[^@]+@[^@]+\.[^@]+')
        if EMAIL_REGEX.fullmatch(email):
            return True
        return False

    @staticmethod
    def cpf_is_valid(cpf):
        """Esta Regex irá aceitar apenas números dentre eles deverão existir . a cada entrada de dados
         e ao fim um único - """
        CPF_REGEX = re.compile('[0-9]+\.[0-9]+\.[0-9]+-[0-9]')
        formated_cpf = re.sub('\D', '', cpf)
        if CPF_REGEX.match(cpf) and len(formated_cpf) == 11:
            return True
        return False

    @staticmethod
    def cpf_convertion(cpf):
        formated_cpf = re.sub('\D', '', cpf)
        return formated_cpf

    @staticmethod
    def date_is_valid(date):
        DATE_REGEX = re.compile('[0-9]+-[0-9]+-[0-9]')
        #datef = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.date.today()
        if DATE_REGEX.match(date) :
            return True
        return False


