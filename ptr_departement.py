from openerp.osv import osv,fields
import openerp

class ptr_departement(osv.osv):
    _name='ptr.departement'
    _columns={
        'name':fields.char('Nom'),
        'code':fields.char('Code'),
        'adresse':fields.char('Adresse'),
        'fixe':fields.char('Telephone fixe'),
        'faxe':fields.char('Faxe'),
        'responsable':fields.char('Responsable'),
        'id_etablissement':fields.many2one('ptr.etablissement','Etablissement',ondelete='cascade'),
        'local_ids':fields.one2many('ptr.local','departement',string='Locaux')
    }
   
ptr_departement()