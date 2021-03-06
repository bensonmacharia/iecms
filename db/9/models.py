# coding: utf-8

# Copyright (C) Nyimbi Odero, 2017-2018

# License: MIT



import datetime

from datetime import datetime, MINYEAR

from flask_appbuilder import Model

from sqlalchemy.dialects.postgresql.base import INTERVAL

from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, Time, text

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

from flask_appbuilder import Model

from sqlalchemy.event import listens_for

from flask import Markup, url_for



from sqlalchemy import func

from flask_appbuilder import Model

from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn, UserExtensionMixin

from flask_appbuilder.models.decorators import renders

from flask_appbuilder.filemanager import ImageManager

from flask_appbuilder.filemanager import get_file_original_name

from sqlalchemy_utils import aggregated, force_auto_coercion, observes

from sqlalchemy.orm import column_property



from flask_appbuilder.filemanager import get_file_original_name

# IMPORT Postgresql Specific Types

from sqlalchemy.dialects.postgresql import (

    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE,

    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER,

    INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT,

    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE,

    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR )



# Versioning and Searchable Mixin

from sqlalchemy_continuum import make_versioned

from sqlalchemy_utils.types import TSVectorType

from sqlalchemy_searchable import make_searchable



from .mixins import *



make_versioned()

make_searchable()



Base = declarative_base()

metadata = Base.metadata

    

from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, String, Table, Text, Time

from sqlalchemy.schema import FetchedValue

from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql.base import INTERVAL

from flask_sqlalchemy import SQLAlchemy





#ENDIMP

db = SQLAlchemy()





#STARTCLASS

class Accounttype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'accounttype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Bill( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'bill'

    __table_args__ = (

         ForeignKeyConstraint(['court_account_courts', 'court_account_account__types'], ['courtaccount.courts', 'courtaccount.account__types']),

         Index('idx_bill__court_account_courts_court_account_account__types', 'court_account_courts', 'court_account_account__types')

    )



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    assessing_registrar =  Column( ForeignKey('judicialofficer.id'), nullable=True, index=True)

    receiving_registrar =  Column( ForeignKey('judicialofficer.id'), nullable=True, index=True)

    lawyer_paying =  Column( ForeignKey('lawyer.id'), index=True)

    party_paying =  Column( ForeignKey('party.complaints'), index=True)

    documents =  Column( ForeignKey('document.id'), index=True)

    date_of_payment =  Column( DateTime)

    paid =  Column( Boolean)

    pay_code =  Column( String(20), unique=True)

    bill_total =  Column( Numeric(12, 2))

    court =  Column( ForeignKey('court.id'), nullable=True, index=True)

    court_account_courts =  Column( Integer, nullable=True)

    court_account_account__types =  Column( Integer, nullable=True)

    validated =  Column( Boolean)

    validation_date =  Column( DateTime)



    judicialofficer =  relationship('Judicialofficer', primaryjoin='Bill.assessing_registrar == Judicialofficer.id', backref='judicialofficer_bills')

    court1 =  relationship('Court', primaryjoin='Bill.court == Court.id', backref='bills')

    courtaccount =  relationship('Courtaccount', primaryjoin='and_(Bill.court_account_courts == Courtaccount.courts, Bill.court_account_account__types == Courtaccount.account__types)', backref='bills')

    document =  relationship('Document', primaryjoin='Bill.documents == Document.id', backref='bills')

    lawyer =  relationship('Lawyer', primaryjoin='Bill.lawyer_paying == Lawyer.id', backref='bills')

    party =  relationship('Party', primaryjoin='Bill.party_paying == Party.complaints', backref='bills')

    judicialofficer1 =  relationship('Judicialofficer', primaryjoin='Bill.receiving_registrar == Judicialofficer.id', backref='judicialofficer_bills_0')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Billdetail( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'billdetail'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    receipt_id =  Column( ForeignKey('bill.id'), nullable=True, index=True)

    feetype =  Column( ForeignKey('feetype.id'), nullable=True, index=True)

    purpose =  Column( Text, nullable=True)

    unit =  Column( Text)

    qty =  Column( Integer)

    unit_cost =  Column( Numeric(12, 2))

    amount =  Column( Numeric(12, 2))



    feetype1 =  relationship('Feetype', primaryjoin='Billdetail.feetype == Feetype.id', backref='billdetails')

    receipt =  relationship('Bill', primaryjoin='Billdetail.receipt_id == Bill.id', backref='billdetails')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Biodatum( ParentageMixin,  BiometricMixin,  PersonMedicalMixin,  PersonDocMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'biodata'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    party =  Column( ForeignKey('party.complaints'), nullable=True, index=True)

    economic_class =  Column( ForeignKey('economicclass.id'), index=True)

    religion =  Column( ForeignKey('religion.id'), index=True)

    photo =  Column( LargeBinary)

    health_status =  Column( Text, nullable=True)



    economicclas =  relationship('Economicclas', primaryjoin='Biodatum.economic_class == Economicclas.id', backref='biodata')

    party1 =  relationship('Party', primaryjoin='Biodatum.party == Party.complaints', backref='biodata')

    religion1 =  relationship('Religion', primaryjoin='Biodatum.religion == Religion.id', backref='biodata')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Casecategory( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'casecategory'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    subcategory =  Column( ForeignKey('casecategory.id'), index=True)



    parent =  relationship('Casecategory', remote_side=[id], primaryjoin='Casecategory.subcategory == Casecategory.id', backref='casecategories')

    casechecklist =  relationship('Casechecklist', secondary='t_casecategorychecklist', backref='casecategories')

    courtcase =  relationship('Courtcase', secondary='t_casecategory_courtcase', backref='casecategories')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_casecategory_courtcase =  Table(

    'casecategory_courtcase',

     Column('casecategory',  ForeignKey('casecategory.id'), primary_key=True, nullable=True),

     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_casecategorychecklist =  Table(

    'casecategorychecklist',

     Column('case_checklists',  ForeignKey('casechecklist.id'), primary_key=True, nullable=True),

     Column('case_categories',  ForeignKey('casecategory.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Casechecklist( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'casechecklist'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    name =  Column( String(100), nullable=True)

    description =  Column( String(100), nullable=True)

    notes =  Column( Text, nullable=True)



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Caselinktype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'caselinktype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Celltype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'celltype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Commital( ActivityMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'commital'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    prisons =  Column( ForeignKey('prison.id'), index=True)

    police_station =  Column( ForeignKey('policestation.id'), index=True)

    parties =  Column( ForeignKey('party.complaints'), nullable=True, index=True)

    casecomplete =  Column( Boolean)

    commit_date =  Column( Date, nullable=True)

    purpose =  Column( Text, nullable=True)

    warrant_type =  Column( ForeignKey('warranttype.id'), nullable=True, index=True)

    warrant_docx =  Column( Text, nullable=True)

    warrant_issue_date =  Column( Date)

    warrant_issued_by =  Column( Text, nullable=True)

    warrant_date_attached =  Column( DateTime)

    duration =  Column( INTERVAL(fields='day to second'))

    commital =  Column( ForeignKey('commital.id'), index=True)

    commital_type =  Column( ForeignKey('commitaltype.id'), nullable=True, index=True)

    court_case =  Column( ForeignKey('courtcase.id'), index=True)

    concurrent =  Column( Boolean)

    life_imprisonment =  Column( Boolean)

    arrival_date =  Column( DateTime)

    sentence_start_date =  Column( DateTime)

    arrest_date =  Column( DateTime)

    remaining_years =  Column( Integer)

    remaining_months =  Column( Integer)

    remaining_days =  Column( Integer)

    cell_number =  Column( Text, nullable=True)

    cell_type =  Column( ForeignKey('celltype.id'), index=True)

    release_date =  Column( DateTime)

    exit_date =  Column( DateTime)

    reason_for_release =  Column( Text, nullable=True)

    with_children =  Column( Boolean)

    release_type =  Column( ForeignKey('releasetype.id'), index=True)

    receiving_officer =  Column( ForeignKey('prisonofficer.id'), nullable=True, index=True)

    releasing_officer =  Column( ForeignKey('prisonofficer.id'), nullable=True, index=True)



    celltype =  relationship('Celltype', primaryjoin='Commital.cell_type == Celltype.id', backref='commitals')

    parent =  relationship('Commital', remote_side=[id], primaryjoin='Commital.commital == Commital.id', backref='commitals')

    commitaltype =  relationship('Commitaltype', primaryjoin='Commital.commital_type == Commitaltype.id', backref='commitals')

    courtcase =  relationship('Courtcase', primaryjoin='Commital.court_case == Courtcase.id', backref='commitals')

    party =  relationship('Party', primaryjoin='Commital.parties == Party.complaints', backref='commitals')

    policestation =  relationship('Policestation', primaryjoin='Commital.police_station == Policestation.id', backref='commitals')

    prison =  relationship('Prison', primaryjoin='Commital.prisons == Prison.id', backref='commitals')

    prisonofficer =  relationship('Prisonofficer', primaryjoin='Commital.receiving_officer == Prisonofficer.id', backref='prisonofficer_commitals')

    releasetype =  relationship('Releasetype', primaryjoin='Commital.release_type == Releasetype.id', backref='commitals')

    prisonofficer1 =  relationship('Prisonofficer', primaryjoin='Commital.releasing_officer == Prisonofficer.id', backref='prisonofficer_commitals_0')

    warranttype =  relationship('Warranttype', primaryjoin='Commital.warrant_type == Warranttype.id', backref='commitals')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Commitaltype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'commitaltype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    maxduration =  Column( INTERVAL(fields='day to second'))



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Complaint( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'complaint'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    active =  Column( Boolean)

    ob_number =  Column( String(20), nullable=True)

    police_station =  Column( ForeignKey('policestation.id'), nullable=True, index=True)

    daterecvd =  Column( DateTime, nullable=True)

    datefiled =  Column( DateTime)

    datecaseopened =  Column( DateTime)

    casesummary =  Column( String(2000), nullable=True)

    complaintstatement =  Column( Text, nullable=True)

    circumstances =  Column( Text, nullable=True)

    reportingofficer =  Column( ForeignKey('policeofficer.id'), nullable=True, index=True)

    casefileinformation =  Column( Text, nullable=True)

    p_request_help =  Column( Boolean)

    p_instruction =  Column( Text, nullable=True)

    p_submitted =  Column( Boolean)

    p_submission_date =  Column( DateTime)

    p_submission_notes =  Column( Text, nullable=True)

    p_closed =  Column( Text, nullable=True)

    p_evaluation =  Column( Text, nullable=True)

    p_recommend_charge =  Column( Boolean)

    charge_sheet =  Column( Text, nullable=True)

    charge_sheet_docx =  Column( Text, nullable=True)

    evaluating_prosecutor_team =  Column( ForeignKey('prosecutorteam.id'), index=True)

    magistrate_report_date =  Column( DateTime)

    reported_to_judicial_officer =  Column( ForeignKey('judicialofficer.id'), index=True)

    closed =  Column( Boolean)

    close_date =  Column( DateTime)

    close_reason =  Column( Text, nullable=True)



    prosecutorteam =  relationship('Prosecutorteam', primaryjoin='Complaint.evaluating_prosecutor_team == Prosecutorteam.id', backref='complaints')

    policestation =  relationship('Policestation', primaryjoin='Complaint.police_station == Policestation.id', backref='complaints')

    judicialofficer =  relationship('Judicialofficer', primaryjoin='Complaint.reported_to_judicial_officer == Judicialofficer.id', backref='complaints')

    policeofficer =  relationship('Policeofficer', primaryjoin='Complaint.reportingofficer == Policeofficer.id', backref='complaints')

    complaintcategory =  relationship('Complaintcategory', secondary='t_complaint_complaintcategory', backref='complaints')

    courtcase =  relationship('Courtcase', secondary='t_complaint_courtcase', backref='complaints')





class Party( PersonMixin,  AuditMixin, AllFeaturesMixin, Complaint):

    __versioned__ = {}


    __tablename__ = 'party'



    complaints =  Column( ForeignKey('complaint.id'), primary_key=True)

    statement =  Column( String(1000), nullable=True)

    statementdate =  Column( DateTime)

    complaint_role =  Column( ForeignKey('complaintrole.id'), nullable=True, index=True)

    notes =  Column( Text, nullable=True)

    dateofrepresentation =  Column( DateTime)

    party_type =  Column( ForeignKey('partytype.id'), nullable=True, index=True)

    relative =  Column( ForeignKey('party.complaints'), nullable=True, index=True)

    relationship_type =  Column( Text, nullable=True)

    is_infant =  Column( Boolean)

    is_minor =  Column( Boolean)

    miranda_read =  Column( Boolean)

    miranda_date =  Column( DateTime)

    miranda_witness =  Column( Text, nullable=True)



    complaintrole =  relationship('Complaintrole', primaryjoin='Party.complaint_role == Complaintrole.id', backref='parties')

    partytype =  relationship('Partytype', primaryjoin='Party.party_type == Partytype.id', backref='parties')

    parent =  relationship('Party', remote_side=[complaints], primaryjoin='Party.relative == Party.complaints', backref='parties')

    settlement =  relationship('Settlement', secondary='t_party_settlement', backref='parties')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_complaint_complaintcategory =  Table(

    'complaint_complaintcategory',

     Column('complaint',  ForeignKey('complaint.id'), primary_key=True, nullable=True),

     Column('complaintcategory',  ForeignKey('complaintcategory.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_complaint_courtcase =  Table(

    'complaint_courtcase',

     Column('complaint',  ForeignKey('complaint.id'), primary_key=True, nullable=True),

     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Complaintcategory( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'complaintcategory'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    complaint_category_parent =  Column( ForeignKey('complaintcategory.id'), index=True)



    parent =  relationship('Complaintcategory', remote_side=[id], primaryjoin='Complaintcategory.complaint_category_parent == Complaintcategory.id', backref='complaintcategories')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Complaintrole( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'complaintrole'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Country( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'country'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    name =  Column( Text, nullable=True)



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class County( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'county'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    country =  Column( ForeignKey('country.id'), nullable=True, index=True)



    country1 =  relationship('Country', primaryjoin='County.country == Country.id', backref='counties')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Court( PlaceMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'court'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    court_rank =  Column( ForeignKey('courtrank.id'), nullable=True, index=True)

    court_station =  Column( ForeignKey('courtstation.id'), nullable=True, index=True)

    town =  Column( ForeignKey('town.id'), nullable=True, index=True)

    till_number =  Column( Text, nullable=True)



    courtrank =  relationship('Courtrank', primaryjoin='Court.court_rank == Courtrank.id', backref='courts')

    courtstation =  relationship('Courtstation', primaryjoin='Court.court_station == Courtstation.id', backref='courts')

    town1 =  relationship('Town', primaryjoin='Court.town == Town.id', backref='courts')

    judicialofficer =  relationship('Judicialofficer', secondary='t_court_judicialofficer', backref='courts')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_court_judicialofficer =  Table(

    'court_judicialofficer',

     Column('court',  ForeignKey('court.id'), primary_key=True, nullable=True),

     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Courtaccount( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'courtaccount'



    courts =  Column( ForeignKey('court.id'), primary_key=True, nullable=True)

    account__types =  Column( ForeignKey('accounttype.id'), primary_key=True, nullable=True, index=True)

    account_number =  Column( Text, nullable=True)

    account_name =  Column( Text, nullable=True)

    short_code =  Column( Text, nullable=True)

    bank_name =  Column( Text, nullable=True)



    accounttype =  relationship('Accounttype', primaryjoin='Courtaccount.account__types == Accounttype.id', backref='courtaccounts')

    court =  relationship('Court', primaryjoin='Courtaccount.courts == Court.id', backref='courtaccounts')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Courtcase( ActivityMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'courtcase'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    docket_number =  Column( Text, nullable=True)

    case_number =  Column( Text, nullable=True)

    adr =  Column( Boolean)

    mediation_proposal =  Column( Text, nullable=True)

    case_received_date =  Column( Date)

    case_filed_date =  Column( Date)

    case_summary =  Column( Text, nullable=True)

    filing_prosecutor =  Column( ForeignKey('prosecutor.id'), index=True)

    fast_track =  Column( Boolean)

    priority =  Column( Integer)

    object_of_litigation =  Column( Text, nullable=True)

    grounds =  Column( Text, nullable=True)

    prosecution_prayer =  Column( Text, nullable=True)

    pretrial_date =  Column( Date)

    pretrial_notes =  Column( Text, nullable=True)

    pretrial_registrar =  Column( ForeignKey('judicialofficer.id'), index=True)

    case_admissible =  Column( Boolean)

    indictment_date =  Column( Text, nullable=True)

    judgement =  Column( Text, nullable=True)

    judgement_docx =  Column( Text, nullable=True)

    case_link_type =  Column( ForeignKey('caselinktype.id'), index=True)

    linked_cases =  Column( ForeignKey('courtcase.id'), index=True)

    appealed =  Column( Boolean)

    appeal_number =  Column( Text, nullable=True)

    inventory_of_docket =  Column( Text, nullable=True)

    next_hearing_date =  Column( Date)

    interlocutory_judgement =  Column( Text, nullable=True)

    reopen =  Column( Boolean)

    reopen_reason =  Column( Text, nullable=True)

    combined_case =  Column( Boolean)

    value_in_dispute =  Column( Numeric(12, 2))

    award =  Column( Numeric(12, 2))

    govt_liability =  Column( Text, nullable=True)

    active =  Column( Boolean)

    active_date =  Column( DateTime)



    caselinktype =  relationship('Caselinktype', primaryjoin='Courtcase.case_link_type == Caselinktype.id', backref='courtcases')

    prosecutor =  relationship('Prosecutor', primaryjoin='Courtcase.filing_prosecutor == Prosecutor.id', backref='courtcases')

    parent =  relationship('Courtcase', remote_side=[id], primaryjoin='Courtcase.linked_cases == Courtcase.id', backref='courtcases')

    judicialofficer =  relationship('Judicialofficer', primaryjoin='Courtcase.pretrial_registrar == Judicialofficer.id', backref='judicialofficer_courtcases')

    judicialofficer1 =  relationship('Judicialofficer', secondary='t_courtcase_judicialofficer', backref='judicialofficer_courtcases_0')

    lawfirm =  relationship('Lawfirm', secondary='t_courtcase_lawfirm', backref='courtcases')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_courtcase_judicialofficer =  Table(

    'courtcase_judicialofficer',

     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True),

     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_courtcase_lawfirm =  Table(

    'courtcase_lawfirm',

     Column('courtcase',  ForeignKey('courtcase.id'), primary_key=True, nullable=True),

     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Courtrank( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'courtrank'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Courtstation( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'courtstation'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    till_number =  Column( Text, nullable=True)

    pay_bill =  Column( Text, nullable=True)



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Crime( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'crime'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    law =  Column( Text, nullable=True)

    description =  Column( Text, nullable=True)

    ref =  Column( Text, nullable=True)

    ref_law =  Column( ForeignKey('law.id'), index=True)



    law1 =  relationship('Law', primaryjoin='Crime.ref_law == Law.id', backref='crimes')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class CsiEquipment( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'csi_equipment'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    investigationdiary =  relationship('Investigationdiary', secondary='t_csi_equipment_investigationdiary', backref='csi_equipments')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_csi_equipment_investigationdiary =  Table(

    'csi_equipment_investigationdiary',

     Column('csi_equipment',  ForeignKey('csi_equipment.id'), primary_key=True, nullable=True),

     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Diagram( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'diagram'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    investigation_diary =  Column( ForeignKey('investigationdiary.id'), nullable=True, index=True)

    image =  Column( Text, nullable=True)

    description =  Column( Text, nullable=True)

    docx =  Column( Text, nullable=True)



    investigationdiary =  relationship('Investigationdiary', primaryjoin='Diagram.investigation_diary == Investigationdiary.id', backref='diagrams')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Discipline( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'discipline'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    party =  Column( ForeignKey('party.complaints'), nullable=True, index=True)

    prison_officer =  Column( ForeignKey('prisonofficer.id'), nullable=True, index=True)



    party1 =  relationship('Party', primaryjoin='Discipline.party == Party.complaints', backref='disciplines')

    prisonofficer =  relationship('Prisonofficer', primaryjoin='Discipline.prison_officer == Prisonofficer.id', backref='disciplines')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Doctemplate( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'doctemplate'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    template =  Column( Text, nullable=True)

    docx =  Column( Text, nullable=True)

    name =  Column( Text, nullable=True)

    title =  Column( Text, nullable=True)

    summary =  Column( Text, nullable=True)

    template_type =  Column( ForeignKey('templatetype.id'), nullable=True, index=True)

    icon =  Column( Text, nullable=True)



    templatetype =  relationship('Templatetype', primaryjoin='Doctemplate.template_type == Templatetype.id', backref='doctemplates')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Document( DocMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'document'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    name =  Column( Text, nullable=True)

    court_case =  Column( ForeignKey('courtcase.id'), index=True)

    issue =  Column( ForeignKey('issue.id'), index=True)

    document_admissibility =  Column( Text, nullable=True)

    admitted =  Column( Boolean)

    judicial_officer =  Column( ForeignKey('judicialofficer.id'), index=True)

    filing_date =  Column( DateTime)

    admisibility_notes =  Column( Text, nullable=True)

    docx =  Column( Text, nullable=True)

    document_text =  Column( Text, nullable=True)

    published =  Column( Boolean)

    publish_newspaper =  Column( Text, nullable=True)

    publish_date =  Column( Date)

    validated =  Column( Boolean)

    paid =  Column( Boolean)

    page_count =  Column( Integer)

    file_byte_count =  Column( Numeric(12, 2))

    file_hash =  Column( Text, nullable=True)

    file_timestamp =  Column( Text, nullable=True)

    file_create_date =  Column( DateTime)

    file_update_date =  Column( DateTime)

    file_text =  Column( Text, nullable=True)

    file_name =  Column( Text, nullable=True)

    file_ext =  Column( Text, nullable=True)

    file_load_path =  Column( Text, nullable=True)

    file_upload_date =  Column( DateTime)

    file_parse_status =  Column( Text, nullable=True)

    doc_template =  Column( ForeignKey('doctemplate.id'), index=True)

    visible =  Column( Boolean)

    is_scan =  Column( Boolean)

    doc_shelf =  Column( Text, nullable=True)

    doc_row =  Column( Text, nullable=True)

    doc_room =  Column( Text, nullable=True)

    doc_placed_by =  Column( Text, nullable=True)

    citation =  Column( Text, nullable=True)



    courtcase =  relationship('Courtcase', primaryjoin='Document.court_case == Courtcase.id', backref='documents')

    doctemplate =  relationship('Doctemplate', primaryjoin='Document.doc_template == Doctemplate.id', backref='documents')

    issue1 =  relationship('Issue', primaryjoin='Document.issue == Issue.id', backref='documents')

    judicialofficer =  relationship('Judicialofficer', primaryjoin='Document.judicial_officer == Judicialofficer.id', backref='documents')

    documenttype =  relationship('Documenttype', secondary='t_document_documenttype', backref='documents')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_document_documenttype =  Table(

    'document_documenttype',

     Column('document',  ForeignKey('document.id'), primary_key=True, nullable=True),

     Column('documenttype',  ForeignKey('documenttype.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Documenttype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'documenttype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Economicclas( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'economicclass'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    name =  Column( String(50), nullable=True)

    description =  Column( String(100), nullable=True)



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Exhibit( DocMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'exhibit'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    investigation_entry =  Column( ForeignKey('investigationdiary.id'), nullable=True, index=True)

    photo =  Column( Text, nullable=True)

    exhibit_no =  Column( Text, nullable=True)

    docx =  Column( Text, nullable=True)

    seizure =  Column( ForeignKey('seizure.id'), nullable=True, index=True)



    investigationdiary =  relationship('Investigationdiary', primaryjoin='Exhibit.investigation_entry == Investigationdiary.id', backref='exhibits')

    seizure1 =  relationship('Seizure', primaryjoin='Exhibit.seizure == Seizure.id', backref='exhibits')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Expert( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'expert'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    institution =  Column( Text, nullable=True)

    jobtitle =  Column( Text, nullable=True)

    credentials =  Column( Text, nullable=True)



    experttype =  relationship('Experttype', secondary='t_expert_experttype', backref='experts')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_expert_experttype =  Table(

    'expert_experttype',

     Column('expert',  ForeignKey('expert.id'), primary_key=True, nullable=True),

     Column('experttype',  ForeignKey('experttype.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Experttestimony( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'experttestimony'



    requesting_officer =  Column( ForeignKey('investigating_officer.police_officers'), nullable=True, index=True)

    investigation_entries =  Column( ForeignKey('investigationdiary.id'), primary_key=True, nullable=True)

    experts =  Column( ForeignKey('expert.id'), primary_key=True, nullable=True, index=True)

    task_given =  Column( Text, nullable=True)

    summary_of_facts =  Column( Text, nullable=True)

    statement =  Column( Text, nullable=True)

    testimony_date =  Column( DateTime)

    task_request_date =  Column( Date)

    docx =  Column( Text, nullable=True)

    validated =  Column( Boolean)



    expert =  relationship('Expert', primaryjoin='Experttestimony.experts == Expert.id', backref='experttestimonies')

    investigationdiary =  relationship('Investigationdiary', primaryjoin='Experttestimony.investigation_entries == Investigationdiary.id', backref='experttestimonies')

    investigating_officer =  relationship('InvestigatingOfficer', primaryjoin='Experttestimony.requesting_officer == InvestigatingOfficer.police_officers', backref='experttestimonies')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Experttype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'experttype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Feeclas( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'feeclass'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    fee_type =  Column( ForeignKey('feeclass.id'), index=True)



    parent =  relationship('Feeclas', remote_side=[id], primaryjoin='Feeclas.fee_type == Feeclas.id', backref='feeclass')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Feetype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'feetype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    filing_fee_type =  Column( ForeignKey('feeclass.id'), nullable=True, index=True)

    amount =  Column( Numeric(12, 2))

    unit =  Column( Text, nullable=True)

    min_fee =  Column( Numeric(12, 2))

    max_fee =  Column( Numeric(12, 2))

    description =  Column( Text)

    guide_sec =  Column( Text)

    guide_clause =  Column( Text)

    account_type =  Column( ForeignKey('accounttype.id'), nullable=True, index=True)



    accounttype =  relationship('Accounttype', primaryjoin='Feetype.account_type == Accounttype.id', backref='feetypes')

    feeclas =  relationship('Feeclas', primaryjoin='Feetype.filing_fee_type == Feeclas.id', backref='feetypes')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Healthevent( ActivityMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'healthevent'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    party =  Column( ForeignKey('party.complaints'), nullable=True, index=True)

    reporting_prison_officer =  Column( ForeignKey('prisonofficer.id'), index=True)

    health_event_type =  Column( ForeignKey('healtheventtype.id'), nullable=True, index=True)

    startdate =  Column( DateTime)

    enddate =  Column( DateTime)

    notes =  Column( Text, nullable=True)



    healtheventtype =  relationship('Healtheventtype', primaryjoin='Healthevent.health_event_type == Healtheventtype.id', backref='healthevents')

    party1 =  relationship('Party', primaryjoin='Healthevent.party == Party.complaints', backref='healthevents')

    prisonofficer =  relationship('Prisonofficer', primaryjoin='Healthevent.reporting_prison_officer == Prisonofficer.id', backref='healthevents')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Healtheventtype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'healtheventtype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Hearing( ActivityMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'hearing'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    court_cases =  Column( ForeignKey('courtcase.id'), index=True)

    hearing_type =  Column( ForeignKey('hearingtype.id'), nullable=True, index=True)

    schedule_status =  Column( ForeignKey('schedulestatustype.id'), nullable=True, index=True)

    hearing_date =  Column( Date)

    reason =  Column( Text, nullable=True)

    sequence =  Column( BigInteger)

    yearday =  Column( BigInteger)

    starttime =  Column( Time)

    endtime =  Column( Time)

    notes =  Column( Text, nullable=True)

    completed =  Column( Boolean)

    adjourned_to =  Column( Date)

    adjournment_reason =  Column( Text, nullable=True)

    transcript =  Column( Text, nullable=True)

    atendance =  Column( Text, nullable=True)

    next_hearing_date =  Column( Date)

    postponement_reason =  Column( Text, nullable=True)



    courtcase =  relationship('Courtcase', primaryjoin='Hearing.court_cases == Courtcase.id', backref='hearings')

    hearingtype =  relationship('Hearingtype', primaryjoin='Hearing.hearing_type == Hearingtype.id', backref='hearings')

    schedulestatustype =  relationship('Schedulestatustype', primaryjoin='Hearing.schedule_status == Schedulestatustype.id', backref='hearings')

    issue =  relationship('Issue', secondary='t_hearing_issue', backref='hearings')

    judicialofficer =  relationship('Judicialofficer', secondary='t_hearing_judicialofficer', backref='hearings')

    lawfirm =  relationship('Lawfirm', secondary='t_hearing_lawfirm', backref='lawfirm_hearings')

    lawfirm1 =  relationship('Lawfirm', secondary='t_hearing_lawfirm_2', backref='lawfirm_hearings_0')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_hearing_issue =  Table(

    'hearing_issue',

     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_hearing_judicialofficer =  Table(

    'hearing_judicialofficer',

     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),

     Column('judicialofficer',  ForeignKey('judicialofficer.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_hearing_lawfirm =  Table(

    'hearing_lawfirm',

     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),

     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_hearing_lawfirm_2 =  Table(

    'hearing_lawfirm_2',

     Column('hearing',  ForeignKey('hearing.id'), primary_key=True, nullable=True),

     Column('lawfirm',  ForeignKey('lawfirm.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Hearingtype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'hearingtype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    hearing_type =  Column( ForeignKey('hearingtype.id'), index=True)



    parent =  relationship('Hearingtype', remote_side=[id], primaryjoin='Hearingtype.hearing_type == Hearingtype.id', backref='hearingtypes')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Instancecrime( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'instancecrime'



    parties =  Column( ForeignKey('party.complaints'), primary_key=True, nullable=True)

    crimes =  Column( ForeignKey('crime.id'), primary_key=True, nullable=True, index=True)

    crime_detail =  Column( Text, nullable=True)

    tffender_type =  Column( Text, nullable=True)

    crime_date =  Column( DateTime)

    date_note =  Column( Text, nullable=True)

    place_of_crime =  Column( Text, nullable=True)

    place_note =  Column( Text, nullable=True)



    crime =  relationship('Crime', primaryjoin='Instancecrime.crimes == Crime.id', backref='instancecrimes')

    party =  relationship('Party', primaryjoin='Instancecrime.parties == Party.complaints', backref='instancecrimes')

    issue =  relationship('Issue', secondary='t_instancecrime_issue', backref='instancecrimes')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_instancecrime_issue =  Table(

    'instancecrime_issue',

     Column('instancecrime_parties',  Integer, primary_key=True, nullable=True),

     Column('instancecrime_crimes',  Integer, primary_key=True, nullable=True),

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True, index=True),

     ForeignKeyConstraint(['instancecrime_parties', 'instancecrime_crimes'], ['instancecrime.parties', 'instancecrime.crimes'])

)



#ENDCLASS





#STARTCLASS

class Interview( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'interview'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    investigation_entry =  Column( ForeignKey('investigationdiary.id'), nullable=True, index=True)

    question =  Column( Text, nullable=True)

    answer =  Column( Text, nullable=True)

    validated =  Column( Boolean)

    language =  Column( Text, nullable=True)



    investigationdiary =  relationship('Investigationdiary', primaryjoin='Interview.investigation_entry == Investigationdiary.id', backref='interviews')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_investigating_officer_investigationdiary =  Table(

    'investigating_officer_investigationdiary',

     Column('investigating_officer',  ForeignKey('investigating_officer.police_officers'), primary_key=True, nullable=True),

     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Investigationdiary( ActivityMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'investigationdiary'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    complaint =  Column( ForeignKey('complaint.id'), nullable=True, index=True)

    activity =  Column( Text, nullable=True)

    location =  Column( Text, nullable=True)

    outcome =  Column( Text, nullable=True)

    equipmentresults =  Column( Text, nullable=True)

    startdate =  Column( DateTime, nullable=True)

    enddate =  Column( DateTime)

    advocate_present =  Column( Text, nullable=True)

    summons_statement =  Column( Text, nullable=True)

    arrest_statement =  Column( Text, nullable=True)

    arrest_warrant =  Column( Text, nullable=True)

    search_seizure_statement =  Column( Text, nullable=True)

    docx =  Column( Text, nullable=True)

    detained =  Column( Text, nullable=True)

    detained_at =  Column( Text, nullable=True)

    provisional_release_statement =  Column( Text, nullable=True)

    warrant_type =  Column( ForeignKey('warranttype.id'), index=True)

    warrant_issued_by =  Column( Text, nullable=True)

    warrant_issue_date =  Column( Date)

    warrant_delivered_by =  Column( Text, nullable=True)

    warrant_received_by =  Column( Text, nullable=True)

    warrant_serve_date =  Column( Text, nullable=True)

    warrant_docx =  Column( Text, nullable=True)

    warrant_upload_date =  Column( Text, nullable=True)



    complaint1 =  relationship('Complaint', primaryjoin='Investigationdiary.complaint == Complaint.id', backref='investigationdiaries')

    warranttype =  relationship('Warranttype', primaryjoin='Investigationdiary.warrant_type == Warranttype.id', backref='investigationdiaries')

    party =  relationship('Party', secondary='t_investigationdiary_party', backref='party_investigationdiaries')

    vehicle =  relationship('Vehicle', secondary='t_investigationdiary_vehicle', backref='investigationdiaries')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_investigationdiary_party =  Table(

    'investigationdiary_party',

     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True),

     Column('party',  ForeignKey('party.complaints'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_investigationdiary_vehicle =  Table(

    'investigationdiary_vehicle',

     Column('investigationdiary',  ForeignKey('investigationdiary.id'), primary_key=True, nullable=True),

     Column('vehicle',  ForeignKey('vehicle.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Issue( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'issue'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    issue =  Column( Text, nullable=True)

    facts =  Column( Text)

    counter_claim =  Column( Boolean)

    argument =  Column( Text, nullable=True)

    argument_date =  Column( Date)

    argument_docx =  Column( Text)

    rebuttal =  Column( Text, nullable=True)

    rebuttal_date =  Column( Date)

    rebuttal_docx =  Column( Text)

    hearing_date =  Column( Date)

    determination =  Column( Text, nullable=True)

    dtermination_date =  Column( Date)

    determination_docx =  Column( Text, nullable=True)

    resolved =  Column( Boolean)

    defense_lawyer =  Column( ForeignKey('lawyer.id'), nullable=True, index=True)

    prosecutor =  Column( ForeignKey('prosecutor.id'), index=True)

    judicial_officer =  Column( ForeignKey('judicialofficer.id'), nullable=True, index=True)

    court_case =  Column( ForeignKey('courtcase.id'), nullable=True, index=True)

    tasks =  Column( Text, nullable=True)

    is_criminal =  Column( Boolean)

    moral_element =  Column( Text, nullable=True)

    material_element =  Column( Text, nullable=True)

    legal_element =  Column( Text, nullable=True)

    debt_amount =  Column( Numeric(12, 2))



    courtcase =  relationship('Courtcase', primaryjoin='Issue.court_case == Courtcase.id', backref='issues')

    lawyer =  relationship('Lawyer', primaryjoin='Issue.defense_lawyer == Lawyer.id', backref='lawyer_issues')

    judicialofficer =  relationship('Judicialofficer', primaryjoin='Issue.judicial_officer == Judicialofficer.id', backref='issues')

    prosecutor1 =  relationship('Prosecutor', primaryjoin='Issue.prosecutor == Prosecutor.id', backref='issues')

    lawyer1 =  relationship('Lawyer', secondary='t_issue_lawyer', backref='lawyer_issues_0')

    legalreference =  relationship('Legalreference', secondary='t_issue_legalreference', backref='legalreference_issues')

    legalreference1 =  relationship('Legalreference', secondary='t_issue_legalreference_2', backref='legalreference_issues_0')

    party =  relationship('Party', secondary='t_issue_party', backref='party_issues')

    party1 =  relationship('Party', secondary='t_issue_party_2', backref='party_issues_0')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_issue_lawyer =  Table(

    'issue_lawyer',

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),

     Column('lawyer',  ForeignKey('lawyer.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_issue_legalreference =  Table(

    'issue_legalreference',

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),

     Column('legalreference',  ForeignKey('legalreference.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_issue_legalreference_2 =  Table(

    'issue_legalreference_2',

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),

     Column('legalreference',  ForeignKey('legalreference.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_issue_party =  Table(

    'issue_party',

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),

     Column('party',  ForeignKey('party.complaints'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

t_issue_party_2 =  Table(

    'issue_party_2',

     Column('issue',  ForeignKey('issue.id'), primary_key=True, nullable=True),

     Column('party',  ForeignKey('party.complaints'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Judicialofficer( PersonMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'judicialofficer'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    rank =  Column( ForeignKey('judicialrank.id'), nullable=True, index=True)

    judicial_role =  Column( ForeignKey('judicialrole.id'), nullable=True, index=True)

    court_station =  Column( ForeignKey('courtstation.id'), nullable=True, index=True)



    courtstation =  relationship('Courtstation', primaryjoin='Judicialofficer.court_station == Courtstation.id', backref='judicialofficers')

    judicialrole =  relationship('Judicialrole', primaryjoin='Judicialofficer.judicial_role == Judicialrole.id', backref='judicialofficers')

    judicialrank =  relationship('Judicialrank', primaryjoin='Judicialofficer.rank == Judicialrank.id', backref='judicialofficers')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Judicialrank( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'judicialrank'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Judicialrole( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'judicialrole'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Law( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'law'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    name =  Column( Text, nullable=True)

    description =  Column( Text, nullable=True)



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Lawfirm( PlaceMixin,  RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'lawfirm'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Lawyer( PersonMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'lawyer'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    law_firm =  Column( ForeignKey('lawfirm.id'), index=True)

    bar_no =  Column( Text, nullable=True)

    bar_date =  Column( Date)



    lawfirm =  relationship('Lawfirm', primaryjoin='Lawyer.law_firm == Lawfirm.id', backref='lawyers')

    party =  relationship('Party', secondary='t_lawyer_party', backref='lawyers')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_lawyer_party =  Table(

    'lawyer_party',

     Column('lawyer',  ForeignKey('lawyer.id'), primary_key=True, nullable=True),

     Column('party',  ForeignKey('party.complaints'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Legalreference( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'legalreference'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    ref =  Column( Text, nullable=True)

    verbatim =  Column( Text, nullable=True)

    public =  Column( Boolean)

    commentary =  Column( Text, nullable=True)

    validated =  Column( Boolean)

    citation =  Column( Text, nullable=True)

    quote =  Column( Text, nullable=True)

    interpretation =  Column( Text, nullable=True)



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Nextofkin( PersonMixin,  PersonDocMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'nextofkin'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    biodata =  Column( ForeignKey('biodata.id'), nullable=True, index=True)

    childunder4 =  Column( Boolean)



    biodatum =  relationship('Biodatum', primaryjoin='Nextofkin.biodata == Biodatum.id', backref='nextofkins')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Notification( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'notification'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    contact =  Column( Text, nullable=True)

    message =  Column( Text, nullable=True)

    confirmation =  Column( Text, nullable=True)

    notification_register =  Column( ForeignKey('notificationregister.id'), index=True)

    add_date =  Column( DateTime)

    send_date =  Column( DateTime)

    sent =  Column( Boolean)

    delivered =  Column( Boolean)

    retries =  Column( Integer)

    abandon =  Column( Boolean)

    retry_count =  Column( Integer)



    notificationregister =  relationship('Notificationregister', primaryjoin='Notification.notification_register == Notificationregister.id', backref='notifications')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Notificationregister( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'notificationregister'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    notification_type =  Column( ForeignKey('notificationtype.id'), nullable=True, index=True)

    contact =  Column( Text, nullable=True)

    notify_event =  Column( ForeignKey('notifyevent.id'), index=True)

    retry_count =  Column( BigInteger)

    active =  Column( Boolean)

    hearing =  Column( ForeignKey('hearing.id'), index=True)

    document =  Column( ForeignKey('document.id'), index=True)

    court_case =  Column( ForeignKey('courtcase.id'), index=True)

    complaint =  Column( ForeignKey('complaint.id'), index=True)

    complaint_category =  Column( ForeignKey('complaintcategory.id'), index=True)

    health_event =  Column( ForeignKey('healthevent.id'), index=True)

    party =  Column( ForeignKey('party.complaints'), index=True)



    complaint1 =  relationship('Complaint', primaryjoin='Notificationregister.complaint == Complaint.id', backref='notificationregisters')

    complaintcategory =  relationship('Complaintcategory', primaryjoin='Notificationregister.complaint_category == Complaintcategory.id', backref='notificationregisters')

    courtcase =  relationship('Courtcase', primaryjoin='Notificationregister.court_case == Courtcase.id', backref='notificationregisters')

    document1 =  relationship('Document', primaryjoin='Notificationregister.document == Document.id', backref='notificationregisters')

    healthevent =  relationship('Healthevent', primaryjoin='Notificationregister.health_event == Healthevent.id', backref='notificationregisters')

    hearing1 =  relationship('Hearing', primaryjoin='Notificationregister.hearing == Hearing.id', backref='notificationregisters')

    notificationtype =  relationship('Notificationtype', primaryjoin='Notificationregister.notification_type == Notificationtype.id', backref='notificationregisters')

    notifyevent =  relationship('Notifyevent', primaryjoin='Notificationregister.notify_event == Notifyevent.id', backref='notificationregisters')

    party1 =  relationship('Party', primaryjoin='Notificationregister.party == Party.complaints', backref='party_notificationregisters')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Notificationtype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'notificationtype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    name =  Column( Text, nullable=True)

    description =  Column( Text, nullable=True)



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Notifyevent( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'notifyevent'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Page( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'page'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    document =  Column( ForeignKey('document.id'), nullable=True, index=True)

    page_image =  Column( LargeBinary)

    page_no =  Column( BigInteger)

    page_text =  Column( Text, nullable=True)

    image_ext =  Column( Text)

    image_width =  Column( Text)

    image_height =  Column( Text)

    create_date =  Column( DateTime)

    update_date =  Column( DateTime)

    upload_dt =  Column( DateTime)



    document1 =  relationship('Document', primaryjoin='Page.document == Document.id', backref='pages')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_party_settlement =  Table(

    'party_settlement',

     Column('party',  ForeignKey('party.complaints'), primary_key=True, nullable=True),

     Column('settlement',  ForeignKey('settlement.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Partytype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'partytype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Payment( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'payment'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    bill =  Column( ForeignKey('bill.id'), nullable=True, index=True)

    amount =  Column( Numeric(12, 2))

    payment_ref =  Column( Text, nullable=True)

    date_paid =  Column( DateTime)

    phone_number =  Column( String(20))

    validated =  Column( Boolean)

    payment_description =  Column( Text)



    bill1 =  relationship('Bill', primaryjoin='Payment.bill == Bill.id', backref='payments')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Personaleffect( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'personaleffect'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    party =  Column( ForeignKey('party.complaints'), nullable=True, index=True)

    personal_effects_category =  Column( ForeignKey('personaleffectscategory.id'), nullable=True, index=True)



    party1 =  relationship('Party', primaryjoin='Personaleffect.party == Party.complaints', backref='personaleffects')

    personaleffectscategory =  relationship('Personaleffectscategory', primaryjoin='Personaleffect.personal_effects_category == Personaleffectscategory.id', backref='personaleffects')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Personaleffectscategory( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'personaleffectscategory'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Policeofficer( PersonMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'policeofficer'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    police_rank =  Column( ForeignKey('policeofficerrank.id'), nullable=True, index=True)

    servicenumber =  Column( String(100), nullable=True, unique=True)



    policeofficerrank =  relationship('Policeofficerrank', primaryjoin='Policeofficer.police_rank == Policeofficerrank.id', backref='policeofficers')

    policestation =  relationship('Policestation', secondary='t_policeofficer_policestation', backref='policeofficers')





class InvestigatingOfficer( AuditMixin, AllFeaturesMixin, Policeofficer):

    __versioned__ = {}


    __tablename__ = 'investigating_officer'



    police_officers =  Column( ForeignKey('policeofficer.id'), primary_key=True)

    date_assigned =  Column( DateTime)

    lead_investigator =  Column( Integer)



    investigationdiary =  relationship('Investigationdiary', secondary='t_investigating_officer_investigationdiary', backref='investigating_officers')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL

    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_policeofficer_policestation =  Table(

    'policeofficer_policestation',

     Column('policeofficer',  ForeignKey('policeofficer.id'), primary_key=True, nullable=True),

     Column('policestation',  ForeignKey('policestation.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Policeofficerrank( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'policeofficerrank'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    name =  Column( Text, nullable=True)

    description =  Column( Text, nullable=True)

    sequence =  Column( Integer)



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Policestation( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'policestation'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    town =  Column( ForeignKey('town.id'), index=True)

    officer_commanding =  Column( ForeignKey('policeofficer.id'), nullable=True, index=True)

    police_station_rank =  Column( ForeignKey('policestationrank.id'), nullable=True, index=True)



    policeofficer =  relationship('Policeofficer', primaryjoin='Policestation.officer_commanding == Policeofficer.id', backref='policestations')

    policestationrank =  relationship('Policestationrank', primaryjoin='Policestation.police_station_rank == Policestationrank.id', backref='policestations')

    town1 =  relationship('Town', primaryjoin='Policestation.town == Town.id', backref='policestations')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Policestationrank( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'policestationrank'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Prison( PlaceMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'prison'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    town =  Column( ForeignKey('town.id'), nullable=True, index=True)



    town1 =  relationship('Town', primaryjoin='Prison.town == Town.id', backref='prisons')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Prisonofficer( PersonMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'prisonofficer'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    prison =  Column( ForeignKey('prison.id'), nullable=True, index=True)

    prison_officer_rank =  Column( ForeignKey('prisonofficerrank.id'), nullable=True, index=True)



    prison1 =  relationship('Prison', primaryjoin='Prisonofficer.prison == Prison.id', backref='prisonofficers')

    prisonofficerrank =  relationship('Prisonofficerrank', primaryjoin='Prisonofficer.prison_officer_rank == Prisonofficerrank.id', backref='prisonofficers')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Prisonofficerrank( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'prisonofficerrank'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Prosecutor( PersonMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'prosecutor'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    prosecutor_team =  Column( ForeignKey('prosecutorteam.id'), index=True)

    lawyer =  Column( ForeignKey('lawyer.id'), nullable=True, index=True)



    lawyer1 =  relationship('Lawyer', primaryjoin='Prosecutor.lawyer == Lawyer.id', backref='prosecutors')

    prosecutorteam =  relationship('Prosecutorteam', primaryjoin='Prosecutor.prosecutor_team == Prosecutorteam.id', backref='prosecutors')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Prosecutorteam( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'prosecutorteam'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Releasetype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'releasetype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Religion( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'religion'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Schedulestatustype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'schedulestatustype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Seizure( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'seizure'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    investigation_diary =  Column( ForeignKey('investigationdiary.id'), nullable=True, index=True)

    owner =  Column( Text, nullable=True)

    item =  Column( Text, nullable=True)

    item_packaging =  Column( Text, nullable=True)

    item_pic =  Column( Text, nullable=True)

    premises =  Column( Text, nullable=True)

    reg_no =  Column( Text, nullable=True)

    witness =  Column( Text, nullable=True)

    notes =  Column( Text, nullable=True)

    docx =  Column( Text, nullable=True)

    item_description =  Column( Text, nullable=True)

    returned =  Column( Boolean)

    return_date =  Column( DateTime)

    return_notes =  Column( Text, nullable=True)

    return_signed_receipt =  Column( Text, nullable=True)

    destroyed =  Column( Boolean)

    destruction_date =  Column( Date)

    destruction_witnesses =  Column( Text, nullable=True)

    destruction_notes =  Column( Text, nullable=True)

    disposed =  Column( Boolean)

    sold_to =  Column( Text, nullable=True)

    disposal_date =  Column( Date)

    disposal_price =  Column( Numeric(12, 2))

    disposal_receipt =  Column( Text, nullable=True)

    recovery_town =  Column( ForeignKey('town.id'), index=True)

    destruction_pic =  Column( Text, nullable=True)

    is_evidence =  Column( Boolean)

    immovable =  Column( Boolean)



    investigationdiary =  relationship('Investigationdiary', primaryjoin='Seizure.investigation_diary == Investigationdiary.id', backref='seizures')

    town =  relationship('Town', primaryjoin='Seizure.recovery_town == Town.id', backref='seizures')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Settlement( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'settlement'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    complaint =  Column( ForeignKey('complaint.id'), nullable=True, index=True)

    terms =  Column( Text, nullable=True)

    amount =  Column( Numeric(12, 2))

    paid =  Column( Boolean)

    docx =  Column( Text, nullable=True)

    settlor =  Column( ForeignKey('party.complaints'), nullable=True, index=True)



    complaint1 =  relationship('Complaint', primaryjoin='Settlement.complaint == Complaint.id', backref='settlements')

    party =  relationship('Party', primaryjoin='Settlement.settlor == Party.complaints', backref='party_settlements')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Subcounty( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'subcounty'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    county =  Column( ForeignKey('county.id'), nullable=True, index=True)



    county1 =  relationship('County', primaryjoin='Subcounty.county == County.id', backref='subcounties')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Templatetype( RefTypeMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'templatetype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    template_type =  Column( ForeignKey('templatetype.id'), index=True)



    parent =  relationship('Templatetype', remote_side=[id], primaryjoin='Templatetype.template_type == Templatetype.id', backref='templatetypes')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Town( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'town'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    ward =  relationship('Ward', secondary='t_town_ward', backref='towns')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

t_town_ward =  Table(

    'town_ward',

     Column('town',  ForeignKey('town.id'), primary_key=True, nullable=True),

     Column('ward',  ForeignKey('ward.id'), primary_key=True, nullable=True, index=True)

)



#ENDCLASS





#STARTCLASS

class Transcript( DocMixin,  AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'transcript'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    video =  Column( Text, nullable=True)

    audio =  Column( Text, nullable=True)

    add_date =  Column( DateTime)

    asr_transcript =  Column( Text, nullable=True)

    asr_date =  Column( DateTime)

    edited_transcript =  Column( Text, nullable=True)

    edit_date =  Column( DateTime)

    certified_transcript =  Column( Text, nullable=True)

    certfiy_date =  Column( DateTime)

    locked =  Column( Boolean)

    hearing =  Column( ForeignKey('hearing.id'), nullable=True, index=True)



    hearing1 =  relationship('Hearing', primaryjoin='Transcript.hearing == Hearing.id', backref='transcripts')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Vehicle( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'vehicle'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    police_station =  Column( ForeignKey('policestation.id'), nullable=True, index=True)

    make =  Column( String(100), nullable=True)

    model =  Column( String(100), nullable=True)

    regno =  Column( String(100), nullable=True)



    policestation =  relationship('Policestation', primaryjoin='Vehicle.police_station == Policestation.id', backref='vehicles')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Ward( AuditMixin, AllFeaturesMixin, Model):

    __versioned__ = {}


    __tablename__ = 'ward'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())

    subcounty =  Column( ForeignKey('subcounty.id'), nullable=True, index=True)



    subcounty1 =  relationship('Subcounty', primaryjoin='Ward.subcounty == Subcounty.id', backref='wards')



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=True)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS





#STARTCLASS

class Warranttype(Model):

    __versioned__ = {}

    __tablename__ = 'warranttype'



    id =  Column( Integer, primary_key=True, server_default= FetchedValue())



    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    file = Column(FileColumn, nullable=False)



    # mindate = datetime.date(MINYEAR, 1, 1)



    def view_name(self):

        return self.__class__.__name__ +'View'



    def photo_img(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')



    def photo_img_thumbnail(self):

        im = ImageManager()

        vn = self.view_name()

        if self.photo:

            return Markup('<a href="' + url_for(vn+'.show', pk=str(self.id)) +

                        '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +

                        '" alt="Photo" class="img-rounded img-responsive"></a>')

        else:

            return Markup('<a href="' + url_for(vn, pk=str(self.id)) +

                        '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')





    def print_button(self):

        vn = self.view_name()

        #pdf = render_pdf(url_for(vn, pk=str(self.id)))

        #pdf = pdfkit.from_string(url_for(vn, pk=str(self.id)))

        #response = make_response(pdf)

        #response.headers['Content-Type'] = 'application/pdf'

        #response.headers['Content-Disposition'] = 'inline; filename=output.pdf'



        return Markup(

            '<a href="' + url_for(vn) + '" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"'+

            'title="Print">' +

            '<i class="fa fa-edit"></i>' +

            '</a>')



    def audio_play(self):

        vn = self.view_name()

        return Markup(

                '<audio controls autoplay>' +

                '<source  src="' + url_for(vn) + '" type="audio/mpeg"'> +'<i class="fa fa-volume-up"></i>' +

                'Your browser does not support the audio element.' +

                '</audio>'

                )



    def download(self):

        vn = self.view_name()

        return Markup(

            '<a href="' + url_for(vn +'.download', filename=str(self.file)) + '">Download</a>')



    def file_name(self):

        return get_file_original_name(str(self.file))



    def month_year(self):

        return datetime.datetime(self.created_on.year, self.created_on.month, 1) #or self.mindate



    def year(self):

        date = self.created_on #or self.mindate

        return datetime.datetime(date.year, 1, 1)#ENDMODEL



#ENDCLASS

