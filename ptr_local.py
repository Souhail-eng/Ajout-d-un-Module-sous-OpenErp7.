from openerp.osv import osv, fields
from openerp import tools

class ptr_local(osv.osv):
    _name='ptr.local'
    _columns={
        'code':fields.char('Code'),
        'designation':fields.char('Designation'),
        'crocquis':fields.binary('Crocquis'),
        'superficie':fields.float('Superficie'),
        'capacite_acceuil':fields.float('Capacite Acceuil'),
        'fiche_immeuble':fields.binary('Fiche Immeuble'),
        'ficheetage':fields.binary('Fiche Etage'),
        'fichelocal':fields.binary('Fiche Local'),
        'departement':fields.many2one('ptr.departement','Departement',ondelete='cascade'),
        'responsable':fields.many2one('ptr.responsable','Responsable', ondelete='cascade')
    }
    
ptr_local()