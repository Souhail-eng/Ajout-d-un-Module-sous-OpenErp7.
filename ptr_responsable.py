from openerp.osv import osv, fields
from openerp import tools

class ptr_responsable(osv.osv):
    _name='ptr.responsable'
    _columns={
        'matricule':fields.char('Matricule'),
        'nom':fields.char('Nom'),
        'prenom':fields.char('Prenom'),
        'fonction':fields.char('Fonction'),
        'tel':fields.char('Telephone'),
        'fax':fields.char('Fax'),
        'email':fields.char('Email'),
        'categoriepersonnel':fields.many2one('ptr.categoriepersonnel','Categorie Personnel'),
        'local_id':fields.many2one('ptr.local','Local',ondelete='cascade')
    }

ptr_responsable()