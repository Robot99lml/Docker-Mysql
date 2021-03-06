from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager
class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    start_date = db.Column(db.DateTime(timezone=False), nullable= True)
    sede_id = db.Column(db.Integer, nullable= True)
    affiliate_id = db.Column(db.String(15), nullable= True)

    def get_response(self, **kwargs):
        """
        Return response
        """
        entity = {
            "id": self.id,
            "start_date": self.start_date.isoformat(timespec='seconds'),
            "sede_id": self.sede_id,
            "affiliate_id": self.affiliate_id
        }
        return entity

class AFI(db.Model):
    """
    Create a AFI table
    """

    __tablename__ = 'AFI'
    
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    IDAFILIADO = db.Column(db.Integer, nullable= True)
    PAPELLIDO = db.Column(db.String(64), nullable= True)
    SAPELLIDO = db.Column(db.String(64), nullable= True)
    PNOMBRE = db.Column(db.String(64), nullable= True)
    SNOMBRE = db.Column(db.String(64), nullable= True)
    TIPO_DOC = db.Column(db.String(15), nullable= True)
    DOCIDAFILIADO = db.Column(db.Integer, nullable= True)
    IDALTERNA = db.Column(db.String(15), nullable= True)
    IDAFILIADOPPAL = db.Column(db.String(15), nullable= True)
    GRUPO_SANG = db.Column(db.String(15), nullable= True)
    ESTADO_CIVIL = db.Column(db.String(15), nullable= True)
    GRUPOETNICO = db.Column(db.String(15), nullable= True)
    SEXO = db.Column(db.String(15), nullable= True)
    IDPARENTESCO = db.Column(db.String(15), nullable= True)
    LOCALIDAD = db.Column(db.String(15), nullable= True)
    DIRECCION = db.Column(db.String(128), nullable= True)
    TELEFONORES = db.Column(db.String(64), nullable= True)
    CIUDAD = db.Column(db.String(15), nullable= True)
    ZONA = db.Column(db.String(15), nullable= True)
    CODENTIDADANTERIOR = db.Column(db.String(15), nullable= True)
    ESTADO = db.Column(db.String(15), nullable= True)
    FECHAULTESTADO = db.Column(db.DateTime(timezone=False), nullable= True)
    IDSEDE = db.Column(db.Integer, nullable= True)
    IDPROVEEDOR = db.Column(db.String(15), nullable= True)
    FNACIMIENTO = db.Column(db.DateTime(timezone=False), nullable= True)
    FECHAAFILSGSSS = db.Column(db.DateTime(timezone=False), nullable= True)
    ACT_ECONO = db.Column(db.String(15), nullable= True)
    IDESCOLARIDAD = db.Column(db.Integer, nullable= True)
    INDCOTIZANTE = db.Column(db.Integer, nullable= True)
    ULTIMOANOAPROBADO = db.Column(db.String(64), nullable= True)
    INCAPACIDADLABORAL = db.Column(db.String(64), nullable= True)
    TIPODISCAPACIDAD = db.Column(db.String(64), nullable= True)
    TIPOAFILIADO = db.Column(db.String(64), nullable= True)
    GRUPOATESPECIAL = db.Column(db.String(64), nullable= True)
    CABEZADEFAMILIA = db.Column(db.String(64), nullable= True)
    ASOCIADO = db.Column(db.String(64), nullable= True)
    TIENEOBS = db.Column(db.String(64), nullable= True)
    CAMPOUSUARIO1 = db.Column(db.String(64), nullable= True)
    FECHAUVISITA = db.Column(db.DateTime(timezone=False), nullable= True)
    CONSANGUINIDAD = db.Column(db.String(64), nullable= True)
    IDADMINISTRADORA = db.Column(db.String(64), nullable= True)
    IDCAUSAL = db.Column(db.String(64), nullable= True)
    FECHACAUSAL = db.Column(db.DateTime(timezone=False), nullable= True)
    CLASIFPC = db.Column(db.String(64), nullable= True)
    NIVELSOCIOEC = db.Column(db.String(64), nullable= True)
    IDPLAN = db.Column(db.Integer, nullable= True)
    FECHAAFILIACION = db.Column(db.DateTime(timezone=False), nullable= True)
    NUMCARNET = db.Column(db.String(64), nullable= True)
    CIUDADDOC = db.Column(db.String(64), nullable= True)
    IDEMPLEADOR = db.Column(db.String(64), nullable= True)
    SEMANASCOT = db.Column(db.String(64), nullable= True)
    CARNETIZADO = db.Column(db.String(64), nullable= True)
    FECHACARNET = db.Column(db.DateTime(timezone=False), nullable= True)
    CONSCERTIFICADO = db.Column(db.String(64), nullable= True)
    CIUDADNAC = db.Column(db.String(64), nullable= True)
    IDOCUPACION = db.Column(db.String(64), nullable= True)
    NACIONALIDAD = db.Column(db.String(64), nullable= True)
    CELULAR = db.Column(db.String(64), nullable= True)
    DIRECCIONLAB = db.Column(db.String(64), nullable= True)
    TELEFONOLAB = db.Column(db.String(64), nullable= True)
    CNSAFIAA = db.Column(db.String(64), nullable= True)
    SISBENNUMFICHA = db.Column(db.String(64), nullable= True)
    SISBENFECHAFICHA = db.Column(db.String(64), nullable= True)
    SISBENPUNTAJE = db.Column(db.String(64), nullable= True)
    SISBENNUCLEOFAM = db.Column(db.String(64), nullable= True)
    SISBENGRUPOB = db.Column(db.String(64), nullable= True)
    IDCONTRATO = db.Column(db.String(64), nullable= True)
    IDBARRIO = db.Column(db.String(64), nullable= True)
    CLASEAFILIACIONARS = db.Column(db.String(64), nullable= True)
    FORMULARIO = db.Column(db.String(64), nullable= True)
    EMAIL  = db.Column(db.String(64), nullable= True)
    NORADICACION = db.Column(db.String(64), nullable= True)
    FECHARADICACION = db.Column(db.DateTime(timezone=False), nullable= True)
    IDTIPOAFILIACION = db.Column(db.Integer, nullable= True)
    IDCLASEAFILIACION = db.Column(db.String(64), nullable= True)
    V_FORMULARIO = db.Column(db.String(64), nullable= True)
    SISBENNIVEL = db.Column(db.String(64), nullable= True)
    CNSXCPA = db.Column(db.String(64), nullable= True)
    FESTADO = db.Column(db.String(64), nullable= True)
    OKBD = db.Column(db.String(64), nullable= True)
    USUARIOBD = db.Column(db.String(64), nullable= True)
    NACIMIENTO = db.Column(db.String(64), nullable= True)
    ITFC = db.Column(db.String(64), nullable= True)
    CNSITFC = db.Column(db.String(64), nullable= True)
    TIPOSUBSIDIO = db.Column(db.String(64), nullable= True)
    COBERTURA_SALUD = db.Column(db.String(64), nullable= True)
    TIPOAFILIADO2 = db.Column(db.String(64), nullable= True)
    IDAFI_TITULAR = db.Column(db.String(64), nullable= True)
    ES_NN = db.Column(db.String(64), nullable= True)
    IDESPECIAL = db.Column(db.String(64), nullable= True)
    MTRIAGE = db.Column(db.String(64), nullable= True)
    FTRIAGE = db.Column(db.String(64), nullable= True)
    GRUPOPOB = db.Column(db.String(64), nullable= True)
    IDSEDETRIAGE = db.Column(db.String(64), nullable= True)
    F_ACTUALIZA = db.Column(db.String(64), nullable= True)
    PRIORIDAD = db.Column(db.String(64), nullable= True)
    URG_NOMBRE = db.Column(db.String(64), nullable= True)
    URG_TELE = db.Column(db.String(64), nullable= True)
    URG_DIR = db.Column(db.String(64), nullable= True)
    URG_VINCULO = db.Column(db.String(64), nullable= True)
    RAIPOSITIVO = db.Column(db.String(64), nullable= True)
    RAIFECHA = db.Column(db.String(64), nullable= True)
    RAIUSU = db.Column(db.String(64), nullable= True)
    USUARIOATIENDE = db.Column(db.String(64), nullable= True)
    OBSERVACION = db.Column(db.String(64), nullable= True)
    PORTABILIDAD = db.Column(db.String(64), nullable= True)
    FIPORT = db.Column(db.String(64), nullable= True)
    FFPORT = db.Column(db.String(64), nullable= True)
    NOMBREAFI = db.Column(db.String(64), nullable= True)
    CORREGIMIENTO = db.Column(db.String(64), nullable= True)
    IDFOTO = db.Column(db.String(64), nullable= True)
    LAT_DIR = db.Column(db.String(64), nullable= True)
    LNG_DIR = db.Column(db.String(64), nullable= True)
    LAT_DIR_L = db.Column(db.String(64), nullable= True)
    LNG_DIR_L = db.Column(db.String(64), nullable= True)
    IDBARRIO_L = db.Column(db.String(64), nullable= True)
    CIUDAD_L = db.Column(db.String(64), nullable= True)
    CORREGIMIENTO_L = db.Column(db.String(64), nullable= True)
    DIR_PPAL = db.Column(db.String(64), nullable= True)
    EDAD = db.Column(db.String(64), nullable= True)
    CLAVE = db.Column(db.String(64), nullable= True)
    PIN = db.Column(db.String(64), nullable= True)
    PROCEDENCIA = db.Column(db.String(64), nullable= True)
    FECHACTIVACION = db.Column(db.DateTime(timezone=False), nullable= True)
    REFDIRPRINC = db.Column(db.String(64), nullable= True)
    REFDIRLAB = db.Column(db.String(64), nullable= True)
    PLANSALUD = db.Column(db.String(64), nullable= True)
    USUPRORROGA = db.Column(db.String(64), nullable= True)
    FECHAPRORROGA = db.Column(db.DateTime(timezone=False), nullable= True)
    CLASEPRORROGA = db.Column(db.String(64), nullable= True)
    CRONICO = db.Column(db.String(64), nullable= True)

    def get_response(self, **kwargs):
        """
        Return response
        """
        entity = {
            'IDAFILIADO': self.IDAFILIADO,
            'PAPELLIDO': self.PAPELLIDO,
            'SAPELLIDO': self.SAPELLIDO,
            'PNOMBRE': self.PNOMBRE,
            'SNOMBRE': self.SNOMBRE,
            'TIPO_DOC': self.TIPO_DOC,
            'DOCIDAFILIADO': self.DOCIDAFILIADO,
            'GRUPO_SANG': self.GRUPO_SANG,
            'ESTADO_CIVIL': self.ESTADO_CIVIL,
            'GRUPOETNICO': self.GRUPOETNICO,
            'SEXO': self.SEXO,
            'DIRECCION': self.DIRECCION,
            'TELEFONORES': self.TELEFONORES,
            'CIUDAD': self.CIUDAD,
            'ZONA': self.ZONA,
            'ESTADO': self.ESTADO,
            'IDSEDE': self.IDSEDE,
            'IDPROVEEDOR': self.IDPROVEEDOR,
            'FNACIMIENTO': self.FNACIMIENTO,
            'NIVELSOCIOEC': self.NIVELSOCIOEC,
            'IDPLAN': self.IDPLAN,
            'NUMCARNET': self.NUMCARNET,
            'CIUDADDOC': self.CIUDADDOC,
            'CIUDADNAC': self.CIUDADNAC,
            'NACIONALIDAD': self.NACIONALIDAD,
            'IDBARRIO': self.IDBARRIO,
            'IDTIPOAFILIACION': self.IDTIPOAFILIACION
        }
        return entity

class SERTOT(db.Model):
    """
        Create a SERTOT table
    """
    __tablename__ = "SERTOT"
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    IDTERCERO = db.Column(db.String(15), nullable= True)
    IDTARIFA = db.Column(db.String(15), nullable= True)
    PREFIJO = db.Column(db.String(15), nullable= True)
    IDSERVICIO = db.Column(db.String(15), nullable= True)
    DESCSERVICIO = db.Column(db.Text, nullable= True)
    SEXO = db.Column(db.String(32), nullable= True)
    VALOR = db.Column(db.Float, nullable= True)
    FACTOR = db.Column(db.Integer, nullable= True)
    IDPLAN = db.Column(db.String(15), nullable= True)
    VLRSERVICIO = db.Column(db.Float, nullable= True)
    CIRUGIA = db.Column(db.Integer, nullable= True)
    PAQUETE = db.Column(db.Integer, nullable= True)
    DETALLADO = db.Column(db.String(64), nullable= True)
    TIPOCONTRATO = db.Column(db.String(64), nullable= True)
    FECHAINIFD = db.Column(db.DateTime(timezone=False), nullable= True)
    FECHAFINFD = db.Column(db.DateTime(timezone=False), nullable= True)
    NIVELFUNCIONARIO = db.Column(db.Integer, nullable= True)
    NIVELSEDE = db.Column(db.Integer, nullable= True)
    MOBSOBLIGATORIA = db.Column(db.String(64), nullable= True)
    POS = db.Column(db.Integer, nullable= True)
    REQAUTORIZACION = db.Column(db.Integer, nullable= True)
    TIPOAUTORIZACION = db.Column(db.String(15), nullable= True)
    IDACUMULADOR = db.Column(db.String(64), nullable= True)
    MEDICAMENTOS = POS = db.Column(db.Integer, nullable= True)
    IDARTICULO = db.Column(db.String(15), nullable= True)
    NIVELATENCION = db.Column(db.Integer, nullable= True)
    IDGENERICO = db.Column(db.String(15), nullable= True)
    FECHAINI = db.Column(db.DateTime(timezone=False), nullable= True)
    FECHAFIN = db.Column(db.DateTime(timezone=False), nullable= True)
    IDTERCEROCA = db.Column(db.Integer, nullable= True)
    IDPLANCA = db.Column(db.Integer, nullable= True)
    REQAUTORIZACIONCA = db.Column(db.Integer, nullable= True)
    IDAREACA = db.Column(db.Integer, nullable= True)
    CODIFICACION = db.Column(db.String(64), nullable= True)
    CODCUPS = db.Column(db.String(15), nullable= True)
    ESTADO = db.Column(db.String(64), nullable= True)

class CIT(db.Model):
    """
    Create a CIT table
    """
    ___tablename__ = 'CIT'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    CONSECUTIVO = db.Column(db.String(15), nullable= True)
    FECHASOL = db.Column(db.DateTime(timezone=False), nullable= True)
    FECHA = db.Column(db.DateTime(timezone=False), nullable= True)
    FECHAATENCION = db.Column(db.DateTime(timezone=False), nullable= True)
    IDAFILIADO = db.Column(db.Integer, nullable= True)
    NUMCARNET = db.Column(db.String(15), nullable= True)
    TIPOCITA = db.Column(db.String(15), nullable= True)
    TIPOSOLICITUD = db.Column(db.String(15), nullable= True)
    IDSERVICIO = db.Column(db.String(15), nullable= True)
    IDSERVICIOPROC = db.Column(db.String(15), nullable= True)
    ATENCION = db.Column(db.String(15), nullable= True)
    PVEZ = db.Column(db.String(15), nullable= True)
    IDCONTRATANTE = db.Column(db.String(15), nullable= True)
    IDSEDE = db.Column(db.Integer, nullable= True)
    IDMEDICO = db.Column(db.String(15), nullable= True)
    IDPLAN = db.Column(db.String(15), nullable= True)
    URGENCIA = db.Column(db.String(15), nullable= True)
    VALORTOTAL = db.Column(db.String(15), nullable= True)
    VALORCOPAGO = db.Column(db.String(15), nullable= True)
    VALOREXEDENTE = db.Column(db.String(15), nullable= True)
    VALORTOTALCOS = db.Column(db.String(15), nullable= True)
    VALORCOPAGOCOSTO = db.Column(db.String(15), nullable= True)
    IMPRESO = db.Column(db.String(15), nullable= True)
    CUMPLIDA = db.Column(db.String(15), nullable= True) 
    IDPESPECIAL = db.Column(db.String(15), nullable= True)
    IDESTADOE = db.Column(db.String(15), nullable= True)
    ESTADO = db.Column(db.String(15), nullable= True)
    CAUSALBLOQUEO = db.Column(db.String(15), nullable= True)
    GENEROCAJA = db.Column(db.String(15), nullable= True)
    IDSEDEATENCION = db.Column(db.String(15), nullable= True)
    TELEFONOAVISO = db.Column(db.String(15), nullable= True)
    IDCAUSAL = db.Column(db.String(15), nullable= True)
    DISPONIBILIDAD = db.Column(db.String(15), nullable= True)
    SPD = db.Column(db.String(15), nullable= True)
    NORECIBOCAJA = db.Column(db.String(15), nullable= True)
    CLASEORDEN = db.Column(db.String(15), nullable= True)
    USUARIO = db.Column(db.String(15), nullable= True)
    NOADMISION = db.Column(db.String(15), nullable= True)
    GENPRESTACION = db.Column(db.String(15), nullable= True)
    FINCONSULTA = db.Column(db.String(15), nullable= True)
    CODCAJA = db.Column(db.String(15), nullable= True)
    FECHALLEGA = db.Column(db.DateTime(timezone=False), nullable= True)
    USUARIOLLEGA = db.Column(db.String(15), nullable= True)
    OBSERVACIONES = db.Column(db.String(15), nullable= True)
    NOAUTORIZACION = db.Column(db.String(15), nullable= True)
    IDSEDEORIGEN = db.Column(db.String(15), nullable= True)
    IDIPSSOLICITA = db.Column(db.String(15), nullable= True)
    IDMEDICOSOLICITA = db.Column(db.String(15), nullable= True)
    AUTORIZADOPOR = db.Column(db.String(15), nullable= True)
    FECHAAUTORIZACION = db.Column(db.DateTime(timezone=False), nullable= True)
    CNSAFIAA = db.Column(db.String(15), nullable= True)
    TIPOCOPAGO = db.Column(db.String(15), nullable= True)
    PROCEDENCIA = db.Column(db.String(15), nullable= True)
    IDAREAH = db.Column(db.String(15), nullable= True)
    IDAREA = db.Column(db.String(15), nullable= True)
    CCOSTO = db.Column(db.String(15), nullable= True)
    SUBCCOSTO = db.Column(db.String(15), nullable= True)
    NIVELATENCION = db.Column(db.String(15), nullable= True)
    FACTURADA = db.Column(db.String(15), nullable= True)
    N_FACTURA = db.Column(db.String(15), nullable= True)
    CNSFCT = db.Column(db.String(15), nullable= True)
    VFACTURAS = db.Column(db.String(15), nullable= True)
    FACTURABLE = db.Column(db.String(15), nullable= True)
    DESCUENTO = db.Column(db.String(15), nullable= True)
    TIPODTO = db.Column(db.String(15), nullable= True)
    MARCAFAC = db.Column(db.String(15), nullable= True)
    IDIPS = db.Column(db.String(15), nullable= True)
    CLASECONTRATO = db.Column(db.String(15), nullable= True)
    ENPAQUETE = db.Column(db.String(15), nullable= True)
    IDCIRUGIA = db.Column(db.String(15), nullable= True)
    CNSFACT = db.Column(db.String(15), nullable= True)
    SOAT = db.Column(db.String(15), nullable= True)
    COPAGOPROPIO = db.Column(db.String(15), nullable= True)
    CNSHACTRAN = db.Column(db.String(15), nullable= True)
    ALTOCOSTO = db.Column(db.String(15), nullable= True)
    IDDX = db.Column(db.String(15), nullable= True)
    IDEMEDICA = db.Column(db.String(15), nullable= True)
    IDTERCEROCA = db.Column(db.String(15), nullable= True)
    FINALIDAD = db.Column(db.String(15), nullable= True)
    TIPOCAJA = db.Column(db.String(15), nullable= True)
    CONSECUTIVOHCA = db.Column(db.String(15), nullable= True)
    AQUIENCOBRO = db.Column(db.String(15), nullable= True)
    VALORPROV = db.Column(db.String(15), nullable= True)
    CODUNG = db.Column(db.String(15), nullable= True)
    CODPRG = db.Column(db.String(15), nullable= True)
    NOCITA= db.Column(db.String(15), nullable= True)
    REASIGNADA = db.Column(db.String(15), nullable= True)
    IDCONTRATO = db.Column(db.String(15), nullable= True)
    ITFC = db.Column(db.String(15), nullable= True)
    CNSITFC = db.Column(db.String(15), nullable= True)
    SYS_COMPUTERNAME = db.Column(db.String(15), nullable= True)
    NOCOBRAR = db.Column(db.String(15), nullable= True)
    CCONTRATANTE = db.Column(db.String(15), nullable= True)
    CONTABILIZADA = db.Column(db.String(15), nullable= True)
    NROCOMPROBANTE = db.Column(db.String(15), nullable= True)
    MARCACONT = db.Column(db.String(15), nullable= True)
    QXCONSECUTIVO = db.Column(db.String(15), nullable= True)
    FECHACIRUGIA = db.Column(db.DateTime(timezone=False), nullable= True)
    FECHAREASIG = db.Column(db.DateTime(timezone=False), nullable= True)
    USUARIOREASIG = db.Column(db.String(15), nullable= True)
    CODCUPS = db.Column(db.String(15), nullable= True)
    IDPLAN_AFI = db.Column(db.String(15), nullable= True)
    IDTERCERO_AFI = db.Column(db.String(15), nullable= True)
    NOMBREACOMPA = db.Column(db.String(15), nullable= True)
    TELEFONOACOMPA = db.Column(db.String(15), nullable= True)
    PARENTESCOACOMPA = db.Column(db.String(15), nullable= True)
    NOMBRERESPO = db.Column(db.String(15), nullable= True)
    TELEFONORESPO = db.Column(db.String(15), nullable= True)
    PARENTESCORESPO = db.Column(db.String(15), nullable= True)
    USUARIONOFACTURABLE = db.Column(db.String(15), nullable= True)
    FECHA_NOFAC = db.Column(db.DateTime(timezone=False), nullable= True)
    PVEZANO = db.Column(db.String(15), nullable= True)
    F_REQUERIDA = db.Column(db.String(15), nullable= True)
    RIESGO = db.Column(db.String(15), nullable= True)
    DURACION = db.Column(db.String(15), nullable= True)
    MVARIAS = db.Column(db.String(15), nullable= True)
    NROCITAS = db.Column(db.String(15), nullable= True)
    CNSORIGINAL = db.Column(db.String(15), nullable= True)
    PREGUNTAPOR = db.Column(db.String(15), nullable= True)
    MPLAN = db.Column(db.String(15), nullable= True)
    IDPLANDISP = db.Column(db.String(15), nullable= True)
    WEB = db.Column(db.String(15), nullable= True)
    DIRECCION = db.Column(db.String(15), nullable= True)
    CIUDAD = db.Column(db.String(15), nullable= True)
    CORREGIMIENTO = db.Column(db.String(15), nullable= True)
    LAT_DIR = db.Column(db.String(15), nullable= True)
    LNG_DIR = db.Column(db.String(15), nullable= True)
    IDBARRIO = db.Column(db.String(15), nullable= True)
    MODALIDAD = db.Column(db.String(15), nullable= True)
    TIPOAFILIADO = db.Column(db.String(15), nullable= True)
    IDAUTSE = db.Column(db.String(15), nullable= True)
    COVID = db.Column(db.String(15), nullable= True)
    USUATENCION = db.Column(db.String(15), nullable= True)
    USURESPONSABLE = db.Column(db.String(15), nullable= True)
    USUGENAGENDA = db.Column(db.String(15), nullable= True)
    FGENERACION = db.Column(db.String(15), nullable= True)
    IDKPAGE = db.Column(db.String(15), nullable= True)
    COMERCIAL = db.Column(db.String(15), nullable= True)
    HORADESDE = db.Column(db.String(15), nullable= True)
    HORAHASTA = db.Column(db.String(15), nullable= True)
    RESULTADOLLAMADA = db.Column(db.String(15), nullable= True)
    USUPREANALITICA = db.Column(db.String(15), nullable= True)
    FECHAPREANALITICA = db.Column(db.DateTime(timezone=False), nullable= True)
    FECHAENVIOLAB = db.Column(db.DateTime(timezone=False), nullable= True)
    ESTADOPREANALITICA = db.Column(db.String(15), nullable= True)
    USUNOPROCESA = db.Column(db.String(15), nullable= True)
    FECHANOPROCESA = db.Column(db.DateTime(timezone=False), nullable= True)
    RAZONNOPROCESA = db.Column(db.String(15), nullable= True)
    ESPROGRAMAS = db.Column(db.String(15), nullable= True)
    URLVIDEOLLAMADA = db.Column(db.String(15), nullable= True)
    CANTIDADC = db.Column(db.String(15), nullable= True)

    def get_response(self, **kwargs):
        """
        Return response
        """
        entity = {
            'CONSECUTIVO': self.CONSECUTIVO,
            'FECHA': self.FECHA and self.FECHA.isoformat(timespec='seconds'),
            'TIPOCITA': self.TIPOCITA,
            'IDSEDE': self.IDSEDE,
            'IDMEDICO': self.IDMEDICO,
            'ESTADO': self.ESTADO,
            'CLASEORDEN': self.CLASEORDEN,
            'USUARIO': self.USUARIO,
            'FECHAAUTORIZACION': self.FECHAAUTORIZACION and self.FECHAAUTORIZACION.isoformat(timespec='seconds')
        }
        return entity