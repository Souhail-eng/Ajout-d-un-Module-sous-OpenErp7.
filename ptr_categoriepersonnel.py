import csv
import psycopg2
import openerp.exceptions
from openerp.osv import osv, fields,orm
from openerp import tools
from datetime import datetime
from dateutil.relativedelta import relativedelta
from operator import itemgetter
import time

import openerp
from openerp import SUPERUSER_ID
from openerp import pooler, tools
from openerp.osv import fields, osv, expression
from openerp.tools.translate import _


class ptr_categoriepersonnel(osv.osv):

	_name = 'ptr.categoriepersonnel'
	_description = "Classe des categories de personnel"
	_rec_name = 'libelle'
	_columns = {
        'code': fields.char('Code'),
        'libelle': fields.char('Libelle'),
        'effective': fields.float('Effective')
	}
    
ptr_categoriepersonnel()