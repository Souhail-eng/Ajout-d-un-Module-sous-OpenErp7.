from openerp.osv import osv, fields
from openerp import tools

class ptr_typeptrgeo(osv.osv):
    _name='ptr.typeptrgeo'
    _columns={
        'code':fields.char('Code'),
        'libelle':fields.char('libelle')
    }
    
ptr_typeptrgeo()