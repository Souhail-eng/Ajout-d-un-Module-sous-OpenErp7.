from openerp.osv import osv,fields
import openerp
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

class ptr_etablissement(osv.osv):
    _name='ptr.etablissement'
    _columns={
        'name':fields.char('Nom',size=128),
        'code':fields.char('Code',size=64),
        'adresse':fields.char('Adresse'),
        'fixe':fields.char('Telephone Fixe'),
        'faxe':fields.char('Faxe'),
        'departement_ids':fields.one2many('ptr.departement','id_etablissement',string='Departement'),
        'inv_ids':fields.one2many('ptr.inv','id_inv',string='Inventaire')
    }
    
ptr_etablissement()
