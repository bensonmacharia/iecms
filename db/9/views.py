# coding: utf-8
# Copyright (C) Nyimbi Odero, 2017-2018
# Generated on 2018-02-05 21:47:31


import calendar
from flask import redirect, flash, url_for, Markup, g
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView, BaseView, MasterDetailView, MultipleView, RestCRUDView, CompactCRUDMixin
from flask_appbuilder import ModelView, CompactCRUDMixin, aggregate_count, action, expose, BaseView, has_access
from flask_appbuilder.charts.views import ChartView, TimeChartView, GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.widgets import ListThumbnail, ListWidget
from flask_appbuilder.widgets import FormVerticalWidget, FormInlineWidget, FormHorizontalWidget, ShowBlockWidget
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction as FA
from flask_appbuilder.models.group import aggregate_count, aggregate_sum, aggregate_avg
from flask_babel import gettext
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms_alchemy import ModelForm
from flask_appbuilder.filemanager import get_file_original_name
from flask_appbuilder.models.mixins import AuditMixin, FileColumn

# To Extend the User Model
from flask_appbuilder.security.views import UserDBModelView
#from flask_babelpkg import lazy_gettext

from app import appbuilder, db
from .models import *


audit_exclude_columns = hide_list = ['created_by', 'changed_by', 'created_on', 'changed_on']

#To pretty Print from PersonMixin
def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)
 
def get_user():
    return g.user
    
def pretty_year(value):
    return str(value.year)
    
def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)
    
# Class of readonly field widgets
class BS3TextFieldROWidget(BS3TextFieldWidget):
    def __call__(self, field, **kwargs):
        kwargs['readonly'] = 'true'
        return super(BS3TextFieldROWidget, self).__call__(field, **kwargs)
        
# Use like this
# class ExampleView(ModelView):
#     datamodel = SQLAInterface(ExampleModel)
#     edit_form_extra_fields = {'field2': TextField('field2',
#                                 widget=BS3TextFieldROWidget())}




####################
# Field Sets and Columns
####################

audit_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on']
add_exclude_columns = edit_exclude_columns = audit_exclude_columns
person_search_exclude_columns = ['photo', 'photo_img', 'photo_img_thumbnail', 'fp_l1', 'fp_l2', 'fp_l3', 'fp_l4',
                                 'fp_l5', 'fp_r1', 'fp_r2', 'fp_r3', 'fp_r4',
                                 'fp_r5'] + ['finger_palm_left', 'finger_palm_right', 'eye_left', 'eye_right']
biometric_columns = ['fp_lthumb', 'fp_left2', 'fp_left3', 'fp_left4', 'fp_left5',
                     'fp_rthumb', 'fp_right2', 'fp_right3', 'fp_right4', 'fp_right5',
                     'palm_left', 'palm_right', 'eye_left', 'eye_right']



Accounttype_add_columns = ['metadata', 'mindate', 'photo']


Accounttype_edit_columns = ['metadata', 'mindate', 'photo']


Accounttype_list_columns = ['metadata', 'mindate', 'photo']


Accounttype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Accounttype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Accounttype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



AuditMixin_add_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on']


AuditMixin_edit_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on']


AuditMixin_list_columns = ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on']


AuditMixin_add_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



AuditMixin_edit_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



AuditMixin_show_field_set = [
    ('Data', {'fields': ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Bill_add_columns = ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date']


Bill_edit_columns = ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date']


Bill_list_columns = ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date']


Bill_add_field_set = [
    ('Data', {'fields': ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Bill_edit_field_set = [
    ('Data', {'fields': ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Bill_show_field_set = [
    ('Data', {'fields': ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Billdetail_add_columns = ['amount', 'feetype', 'feetype1', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']


Billdetail_edit_columns = ['amount', 'feetype', 'feetype1', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']


Billdetail_list_columns = ['amount', 'feetype', 'feetype1', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']


Billdetail_add_field_set = [
    ('Data', {'fields': ['amount', 'feetype', 'feetype1', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Billdetail_edit_field_set = [
    ('Data', {'fields': ['amount', 'feetype', 'feetype1', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Billdetail_show_field_set = [
    ('Data', {'fields': ['amount', 'feetype', 'feetype1', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Biodatum_add_columns = ['economic_class', 'economicclas', 'health_status', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1']


Biodatum_edit_columns = ['economic_class', 'economicclas', 'health_status', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1']


Biodatum_list_columns = ['economic_class', 'economicclas', 'health_status', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1']


Biodatum_add_field_set = [
    ('Data', {'fields': ['economic_class', 'economicclas', 'health_status', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Biodatum_edit_field_set = [
    ('Data', {'fields': ['economic_class', 'economicclas', 'health_status', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Biodatum_show_field_set = [
    ('Data', {'fields': ['economic_class', 'economicclas', 'health_status', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casecategory_add_columns = ['casechecklist', 'courtcase', 'metadata', 'mindate', 'parent', 'photo', 'subcategory']


Casecategory_edit_columns = ['casechecklist', 'courtcase', 'metadata', 'mindate', 'parent', 'photo', 'subcategory']


Casecategory_list_columns = ['casechecklist', 'courtcase', 'metadata', 'mindate', 'parent', 'photo', 'subcategory']


Casecategory_add_field_set = [
    ('Data', {'fields': ['casechecklist', 'courtcase', 'metadata', 'mindate', 'parent', 'photo', 'subcategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casecategory_edit_field_set = [
    ('Data', {'fields': ['casechecklist', 'courtcase', 'metadata', 'mindate', 'parent', 'photo', 'subcategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casecategory_show_field_set = [
    ('Data', {'fields': ['casechecklist', 'courtcase', 'metadata', 'mindate', 'parent', 'photo', 'subcategory'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casechecklist_add_columns = ['description', 'metadata', 'mindate', 'name', 'notes', 'photo']


Casechecklist_edit_columns = ['description', 'metadata', 'mindate', 'name', 'notes', 'photo']


Casechecklist_list_columns = ['description', 'metadata', 'mindate', 'name', 'notes', 'photo']


Casechecklist_add_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'notes', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casechecklist_edit_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'notes', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Casechecklist_show_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'notes', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Caselinktype_add_columns = ['metadata', 'mindate', 'photo']


Caselinktype_edit_columns = ['metadata', 'mindate', 'photo']


Caselinktype_list_columns = ['metadata', 'mindate', 'photo']


Caselinktype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Caselinktype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Caselinktype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Celltype_add_columns = ['metadata', 'mindate', 'photo']


Celltype_edit_columns = ['metadata', 'mindate', 'photo']


Celltype_list_columns = ['metadata', 'mindate', 'photo']


Celltype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Celltype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Celltype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commital_add_columns = ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']


Commital_edit_columns = ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']


Commital_list_columns = ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']


Commital_add_field_set = [
    ('Data', {'fields': ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commital_edit_field_set = [
    ('Data', {'fields': ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commital_show_field_set = [
    ('Data', {'fields': ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commitaltype_add_columns = ['maxduration', 'metadata', 'mindate', 'photo']


Commitaltype_edit_columns = ['maxduration', 'metadata', 'mindate', 'photo']


Commitaltype_list_columns = ['maxduration', 'metadata', 'mindate', 'photo']


Commitaltype_add_field_set = [
    ('Data', {'fields': ['maxduration', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commitaltype_edit_field_set = [
    ('Data', {'fields': ['maxduration', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Commitaltype_show_field_set = [
    ('Data', {'fields': ['maxduration', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaint_add_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']


Complaint_edit_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']


Complaint_list_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']


Complaint_add_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaint_edit_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaint_show_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintcategory_add_columns = ['complaint_category_parent', 'metadata', 'mindate', 'parent', 'photo']


Complaintcategory_edit_columns = ['complaint_category_parent', 'metadata', 'mindate', 'parent', 'photo']


Complaintcategory_list_columns = ['complaint_category_parent', 'metadata', 'mindate', 'parent', 'photo']


Complaintcategory_add_field_set = [
    ('Data', {'fields': ['complaint_category_parent', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintcategory_edit_field_set = [
    ('Data', {'fields': ['complaint_category_parent', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintcategory_show_field_set = [
    ('Data', {'fields': ['complaint_category_parent', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintrole_add_columns = ['metadata', 'mindate', 'photo']


Complaintrole_edit_columns = ['metadata', 'mindate', 'photo']


Complaintrole_list_columns = ['metadata', 'mindate', 'photo']


Complaintrole_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintrole_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Complaintrole_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Country_add_columns = ['metadata', 'mindate', 'name', 'photo']


Country_edit_columns = ['metadata', 'mindate', 'name', 'photo']


Country_list_columns = ['metadata', 'mindate', 'name', 'photo']


Country_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Country_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Country_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



County_add_columns = ['country', 'country1', 'metadata', 'mindate', 'photo']


County_edit_columns = ['country', 'country1', 'metadata', 'mindate', 'photo']


County_list_columns = ['country', 'country1', 'metadata', 'mindate', 'photo']


County_add_field_set = [
    ('Data', {'fields': ['country', 'country1', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



County_edit_field_set = [
    ('Data', {'fields': ['country', 'country1', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



County_show_field_set = [
    ('Data', {'fields': ['country', 'country1', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Court_add_columns = ['court_rank', 'court_station', 'courtrank', 'courtstation', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1']


Court_edit_columns = ['court_rank', 'court_station', 'courtrank', 'courtstation', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1']


Court_list_columns = ['court_rank', 'court_station', 'courtrank', 'courtstation', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1']


Court_add_field_set = [
    ('Data', {'fields': ['court_rank', 'court_station', 'courtrank', 'courtstation', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Court_edit_field_set = [
    ('Data', {'fields': ['court_rank', 'court_station', 'courtrank', 'courtstation', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Court_show_field_set = [
    ('Data', {'fields': ['court_rank', 'court_station', 'courtrank', 'courtstation', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtaccount_add_columns = ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'metadata', 'mindate', 'photo', 'short_code']


Courtaccount_edit_columns = ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'metadata', 'mindate', 'photo', 'short_code']


Courtaccount_list_columns = ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'metadata', 'mindate', 'photo', 'short_code']


Courtaccount_add_field_set = [
    ('Data', {'fields': ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'metadata', 'mindate', 'photo', 'short_code'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtaccount_edit_field_set = [
    ('Data', {'fields': ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'metadata', 'mindate', 'photo', 'short_code'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtaccount_show_field_set = [
    ('Data', {'fields': ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'metadata', 'mindate', 'photo', 'short_code'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtcase_add_columns = ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'filing_prosecutor', 'govt_liability', 'grounds', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute']


Courtcase_edit_columns = ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'filing_prosecutor', 'govt_liability', 'grounds', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute']


Courtcase_list_columns = ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'filing_prosecutor', 'govt_liability', 'grounds', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute']


Courtcase_add_field_set = [
    ('Data', {'fields': ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'filing_prosecutor', 'govt_liability', 'grounds', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtcase_edit_field_set = [
    ('Data', {'fields': ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'filing_prosecutor', 'govt_liability', 'grounds', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtcase_show_field_set = [
    ('Data', {'fields': ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'filing_prosecutor', 'govt_liability', 'grounds', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtrank_add_columns = ['metadata', 'mindate', 'photo']


Courtrank_edit_columns = ['metadata', 'mindate', 'photo']


Courtrank_list_columns = ['metadata', 'mindate', 'photo']


Courtrank_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtrank_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtrank_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtstation_add_columns = ['metadata', 'mindate', 'pay_bill', 'photo', 'till_number']


Courtstation_edit_columns = ['metadata', 'mindate', 'pay_bill', 'photo', 'till_number']


Courtstation_list_columns = ['metadata', 'mindate', 'pay_bill', 'photo', 'till_number']


Courtstation_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'pay_bill', 'photo', 'till_number'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtstation_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'pay_bill', 'photo', 'till_number'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Courtstation_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'pay_bill', 'photo', 'till_number'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Crime_add_columns = ['description', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law']


Crime_edit_columns = ['description', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law']


Crime_list_columns = ['description', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law']


Crime_add_field_set = [
    ('Data', {'fields': ['description', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Crime_edit_field_set = [
    ('Data', {'fields': ['description', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Crime_show_field_set = [
    ('Data', {'fields': ['description', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



CsiEquipment_add_columns = ['investigationdiary', 'metadata', 'mindate', 'photo']


CsiEquipment_edit_columns = ['investigationdiary', 'metadata', 'mindate', 'photo']


CsiEquipment_list_columns = ['investigationdiary', 'metadata', 'mindate', 'photo']


CsiEquipment_add_field_set = [
    ('Data', {'fields': ['investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



CsiEquipment_edit_field_set = [
    ('Data', {'fields': ['investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



CsiEquipment_show_field_set = [
    ('Data', {'fields': ['investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Diagram_add_columns = ['description', 'docx', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo']


Diagram_edit_columns = ['description', 'docx', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo']


Diagram_list_columns = ['description', 'docx', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo']


Diagram_add_field_set = [
    ('Data', {'fields': ['description', 'docx', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Diagram_edit_field_set = [
    ('Data', {'fields': ['description', 'docx', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Diagram_show_field_set = [
    ('Data', {'fields': ['description', 'docx', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Discipline_add_columns = ['metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer']


Discipline_edit_columns = ['metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer']


Discipline_list_columns = ['metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer']


Discipline_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Discipline_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Discipline_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Doctemplate_add_columns = ['docx', 'icon', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title']


Doctemplate_edit_columns = ['docx', 'icon', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title']


Doctemplate_list_columns = ['docx', 'icon', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title']


Doctemplate_add_field_set = [
    ('Data', {'fields': ['docx', 'icon', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Doctemplate_edit_field_set = [
    ('Data', {'fields': ['docx', 'icon', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Doctemplate_show_field_set = [
    ('Data', {'fields': ['docx', 'icon', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Document_add_columns = ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible']


Document_edit_columns = ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible']


Document_list_columns = ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible']


Document_add_field_set = [
    ('Data', {'fields': ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Document_edit_field_set = [
    ('Data', {'fields': ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Document_show_field_set = [
    ('Data', {'fields': ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Documenttype_add_columns = ['metadata', 'mindate', 'photo']


Documenttype_edit_columns = ['metadata', 'mindate', 'photo']


Documenttype_list_columns = ['metadata', 'mindate', 'photo']


Documenttype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Documenttype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Documenttype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Economicclas_add_columns = ['description', 'metadata', 'mindate', 'name', 'photo']


Economicclas_edit_columns = ['description', 'metadata', 'mindate', 'name', 'photo']


Economicclas_list_columns = ['description', 'metadata', 'mindate', 'name', 'photo']


Economicclas_add_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Economicclas_edit_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Economicclas_show_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Exhibit_add_columns = ['docx', 'exhibit_no', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1']


Exhibit_edit_columns = ['docx', 'exhibit_no', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1']


Exhibit_list_columns = ['docx', 'exhibit_no', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1']


Exhibit_add_field_set = [
    ('Data', {'fields': ['docx', 'exhibit_no', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Exhibit_edit_field_set = [
    ('Data', {'fields': ['docx', 'exhibit_no', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Exhibit_show_field_set = [
    ('Data', {'fields': ['docx', 'exhibit_no', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Expert_add_columns = ['credentials', 'experttype', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo']


Expert_edit_columns = ['credentials', 'experttype', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo']


Expert_list_columns = ['credentials', 'experttype', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo']


Expert_add_field_set = [
    ('Data', {'fields': ['credentials', 'experttype', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Expert_edit_field_set = [
    ('Data', {'fields': ['credentials', 'experttype', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Expert_show_field_set = [
    ('Data', {'fields': ['credentials', 'experttype', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttestimony_add_columns = ['docx', 'expert', 'experts', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']


Experttestimony_edit_columns = ['docx', 'expert', 'experts', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']


Experttestimony_list_columns = ['docx', 'expert', 'experts', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']


Experttestimony_add_field_set = [
    ('Data', {'fields': ['docx', 'expert', 'experts', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttestimony_edit_field_set = [
    ('Data', {'fields': ['docx', 'expert', 'experts', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttestimony_show_field_set = [
    ('Data', {'fields': ['docx', 'expert', 'experts', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttype_add_columns = ['metadata', 'mindate', 'photo']


Experttype_edit_columns = ['metadata', 'mindate', 'photo']


Experttype_list_columns = ['metadata', 'mindate', 'photo']


Experttype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Experttype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feeclas_add_columns = ['fee_type', 'metadata', 'mindate', 'parent', 'photo']


Feeclas_edit_columns = ['fee_type', 'metadata', 'mindate', 'parent', 'photo']


Feeclas_list_columns = ['fee_type', 'metadata', 'mindate', 'parent', 'photo']


Feeclas_add_field_set = [
    ('Data', {'fields': ['fee_type', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feeclas_edit_field_set = [
    ('Data', {'fields': ['fee_type', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feeclas_show_field_set = [
    ('Data', {'fields': ['fee_type', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feetype_add_columns = ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'filing_fee_type', 'guide_clause', 'guide_sec', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit']


Feetype_edit_columns = ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'filing_fee_type', 'guide_clause', 'guide_sec', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit']


Feetype_list_columns = ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'filing_fee_type', 'guide_clause', 'guide_sec', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit']


Feetype_add_field_set = [
    ('Data', {'fields': ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'filing_fee_type', 'guide_clause', 'guide_sec', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feetype_edit_field_set = [
    ('Data', {'fields': ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'filing_fee_type', 'guide_clause', 'guide_sec', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Feetype_show_field_set = [
    ('Data', {'fields': ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'filing_fee_type', 'guide_clause', 'guide_sec', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FetchedValue_add_columns = ['dispatch', 'has_argument', 'is_server_default', 'reflected']


FetchedValue_edit_columns = ['dispatch', 'has_argument', 'is_server_default', 'reflected']


FetchedValue_list_columns = ['dispatch', 'has_argument', 'is_server_default', 'reflected']


FetchedValue_add_field_set = [
    ('Data', {'fields': ['dispatch', 'has_argument', 'is_server_default', 'reflected'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FetchedValue_edit_field_set = [
    ('Data', {'fields': ['dispatch', 'has_argument', 'is_server_default', 'reflected'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FetchedValue_show_field_set = [
    ('Data', {'fields': ['dispatch', 'has_argument', 'is_server_default', 'reflected'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FileColumn_add_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


FileColumn_edit_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


FileColumn_list_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


FileColumn_add_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FileColumn_edit_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



FileColumn_show_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healthevent_add_columns = ['enddate', 'health_event_type', 'healtheventtype', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate']


Healthevent_edit_columns = ['enddate', 'health_event_type', 'healtheventtype', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate']


Healthevent_list_columns = ['enddate', 'health_event_type', 'healtheventtype', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate']


Healthevent_add_field_set = [
    ('Data', {'fields': ['enddate', 'health_event_type', 'healtheventtype', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healthevent_edit_field_set = [
    ('Data', {'fields': ['enddate', 'health_event_type', 'healtheventtype', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healthevent_show_field_set = [
    ('Data', {'fields': ['enddate', 'health_event_type', 'healtheventtype', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healtheventtype_add_columns = ['metadata', 'mindate', 'photo']


Healtheventtype_edit_columns = ['metadata', 'mindate', 'photo']


Healtheventtype_list_columns = ['metadata', 'mindate', 'photo']


Healtheventtype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healtheventtype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Healtheventtype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearing_add_columns = ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'hearing_date', 'hearing_type', 'hearingtype', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday']


Hearing_edit_columns = ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'hearing_date', 'hearing_type', 'hearingtype', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday']


Hearing_list_columns = ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'hearing_date', 'hearing_type', 'hearingtype', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday']


Hearing_add_field_set = [
    ('Data', {'fields': ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'hearing_date', 'hearing_type', 'hearingtype', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearing_edit_field_set = [
    ('Data', {'fields': ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'hearing_date', 'hearing_type', 'hearingtype', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearing_show_field_set = [
    ('Data', {'fields': ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'hearing_date', 'hearing_type', 'hearingtype', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearingtype_add_columns = ['hearing_type', 'metadata', 'mindate', 'parent', 'photo']


Hearingtype_edit_columns = ['hearing_type', 'metadata', 'mindate', 'parent', 'photo']


Hearingtype_list_columns = ['hearing_type', 'metadata', 'mindate', 'parent', 'photo']


Hearingtype_add_field_set = [
    ('Data', {'fields': ['hearing_type', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearingtype_edit_field_set = [
    ('Data', {'fields': ['hearing_type', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Hearingtype_show_field_set = [
    ('Data', {'fields': ['hearing_type', 'metadata', 'mindate', 'parent', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageColumn_add_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


ImageColumn_edit_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


ImageColumn_list_columns = ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']


ImageColumn_add_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageColumn_edit_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageColumn_show_field_set = [
    ('Data', {'fields': ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageManager_add_columns = ['keep_image_formats']


ImageManager_edit_columns = ['keep_image_formats']


ImageManager_list_columns = ['keep_image_formats']


ImageManager_add_field_set = [
    ('Data', {'fields': ['keep_image_formats'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageManager_edit_field_set = [
    ('Data', {'fields': ['keep_image_formats'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



ImageManager_show_field_set = [
    ('Data', {'fields': ['keep_image_formats'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Instancecrime_add_columns = ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type']


Instancecrime_edit_columns = ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type']


Instancecrime_list_columns = ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type']


Instancecrime_add_field_set = [
    ('Data', {'fields': ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Instancecrime_edit_field_set = [
    ('Data', {'fields': ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Instancecrime_show_field_set = [
    ('Data', {'fields': ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Interview_add_columns = ['answer', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated']


Interview_edit_columns = ['answer', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated']


Interview_list_columns = ['answer', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated']


Interview_add_field_set = [
    ('Data', {'fields': ['answer', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Interview_edit_field_set = [
    ('Data', {'fields': ['answer', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Interview_show_field_set = [
    ('Data', {'fields': ['answer', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



InvestigatingOfficer_add_columns = ['date_assigned', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


InvestigatingOfficer_edit_columns = ['date_assigned', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


InvestigatingOfficer_list_columns = ['date_assigned', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


InvestigatingOfficer_add_field_set = [
    ('Data', {'fields': ['date_assigned', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



InvestigatingOfficer_edit_field_set = [
    ('Data', {'fields': ['date_assigned', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



InvestigatingOfficer_show_field_set = [
    ('Data', {'fields': ['date_assigned', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Investigationdiary_add_columns = ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']


Investigationdiary_edit_columns = ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']


Investigationdiary_list_columns = ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']


Investigationdiary_add_field_set = [
    ('Data', {'fields': ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Investigationdiary_edit_field_set = [
    ('Data', {'fields': ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Investigationdiary_show_field_set = [
    ('Data', {'fields': ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Issue_add_columns = ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']


Issue_edit_columns = ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']


Issue_list_columns = ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']


Issue_add_field_set = [
    ('Data', {'fields': ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Issue_edit_field_set = [
    ('Data', {'fields': ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Issue_show_field_set = [
    ('Data', {'fields': ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'hearing_date', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialofficer_add_columns = ['court_station', 'courtstation', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank']


Judicialofficer_edit_columns = ['court_station', 'courtstation', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank']


Judicialofficer_list_columns = ['court_station', 'courtstation', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank']


Judicialofficer_add_field_set = [
    ('Data', {'fields': ['court_station', 'courtstation', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialofficer_edit_field_set = [
    ('Data', {'fields': ['court_station', 'courtstation', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialofficer_show_field_set = [
    ('Data', {'fields': ['court_station', 'courtstation', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrank_add_columns = ['metadata', 'mindate', 'photo']


Judicialrank_edit_columns = ['metadata', 'mindate', 'photo']


Judicialrank_list_columns = ['metadata', 'mindate', 'photo']


Judicialrank_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrank_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrank_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrole_add_columns = ['metadata', 'mindate', 'photo']


Judicialrole_edit_columns = ['metadata', 'mindate', 'photo']


Judicialrole_list_columns = ['metadata', 'mindate', 'photo']


Judicialrole_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrole_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Judicialrole_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Law_add_columns = ['description', 'metadata', 'mindate', 'name', 'photo']


Law_edit_columns = ['description', 'metadata', 'mindate', 'name', 'photo']


Law_list_columns = ['description', 'metadata', 'mindate', 'name', 'photo']


Law_add_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Law_edit_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Law_show_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawfirm_add_columns = ['metadata', 'mindate', 'photo']


Lawfirm_edit_columns = ['metadata', 'mindate', 'photo']


Lawfirm_list_columns = ['metadata', 'mindate', 'photo']


Lawfirm_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawfirm_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawfirm_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawyer_add_columns = ['bar_date', 'bar_no', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo']


Lawyer_edit_columns = ['bar_date', 'bar_no', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo']


Lawyer_list_columns = ['bar_date', 'bar_no', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo']


Lawyer_add_field_set = [
    ('Data', {'fields': ['bar_date', 'bar_no', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawyer_edit_field_set = [
    ('Data', {'fields': ['bar_date', 'bar_no', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Lawyer_show_field_set = [
    ('Data', {'fields': ['bar_date', 'bar_no', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Legalreference_add_columns = ['citation', 'commentary', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim']


Legalreference_edit_columns = ['citation', 'commentary', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim']


Legalreference_list_columns = ['citation', 'commentary', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim']


Legalreference_add_field_set = [
    ('Data', {'fields': ['citation', 'commentary', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Legalreference_edit_field_set = [
    ('Data', {'fields': ['citation', 'commentary', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Legalreference_show_field_set = [
    ('Data', {'fields': ['citation', 'commentary', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Markup_add_columns = []


Markup_edit_columns = []


Markup_list_columns = []


Markup_add_field_set = [
    ('Data', {'fields': [], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Markup_edit_field_set = [
    ('Data', {'fields': [], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Markup_show_field_set = [
    ('Data', {'fields': [], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



MetaData_add_columns = ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables']


MetaData_edit_columns = ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables']


MetaData_list_columns = ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables']


MetaData_add_field_set = [
    ('Data', {'fields': ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



MetaData_edit_field_set = [
    ('Data', {'fields': ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



MetaData_show_field_set = [
    ('Data', {'fields': ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Model_add_columns = ['metadata']


Model_edit_columns = ['metadata']


Model_list_columns = ['metadata']


Model_add_field_set = [
    ('Data', {'fields': ['metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Model_edit_field_set = [
    ('Data', {'fields': ['metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Model_show_field_set = [
    ('Data', {'fields': ['metadata'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Nextofkin_add_columns = ['biodata', 'biodatum', 'childunder4', 'metadata', 'mindate', 'photo']


Nextofkin_edit_columns = ['biodata', 'biodatum', 'childunder4', 'metadata', 'mindate', 'photo']


Nextofkin_list_columns = ['biodata', 'biodatum', 'childunder4', 'metadata', 'mindate', 'photo']


Nextofkin_add_field_set = [
    ('Data', {'fields': ['biodata', 'biodatum', 'childunder4', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Nextofkin_edit_field_set = [
    ('Data', {'fields': ['biodata', 'biodatum', 'childunder4', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Nextofkin_show_field_set = [
    ('Data', {'fields': ['biodata', 'biodatum', 'childunder4', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notification_add_columns = ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent']


Notification_edit_columns = ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent']


Notification_list_columns = ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent']


Notification_add_field_set = [
    ('Data', {'fields': ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notification_edit_field_set = [
    ('Data', {'fields': ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notification_show_field_set = [
    ('Data', {'fields': ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationregister_add_columns = ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count']


Notificationregister_edit_columns = ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count']


Notificationregister_list_columns = ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count']


Notificationregister_add_field_set = [
    ('Data', {'fields': ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationregister_edit_field_set = [
    ('Data', {'fields': ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationregister_show_field_set = [
    ('Data', {'fields': ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'health_event', 'healthevent', 'hearing', 'hearing1', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationtype_add_columns = ['description', 'metadata', 'mindate', 'name', 'photo']


Notificationtype_edit_columns = ['description', 'metadata', 'mindate', 'name', 'photo']


Notificationtype_list_columns = ['description', 'metadata', 'mindate', 'name', 'photo']


Notificationtype_add_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationtype_edit_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notificationtype_show_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notifyevent_add_columns = ['metadata', 'mindate', 'photo']


Notifyevent_edit_columns = ['metadata', 'mindate', 'photo']


Notifyevent_list_columns = ['metadata', 'mindate', 'photo']


Notifyevent_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notifyevent_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Notifyevent_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Page_add_columns = ['create_date', 'document', 'document1', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt']


Page_edit_columns = ['create_date', 'document', 'document1', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt']


Page_list_columns = ['create_date', 'document', 'document1', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt']


Page_add_field_set = [
    ('Data', {'fields': ['create_date', 'document', 'document1', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Page_edit_field_set = [
    ('Data', {'fields': ['create_date', 'document', 'document1', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Page_show_field_set = [
    ('Data', {'fields': ['create_date', 'document', 'document1', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Party_add_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate']


Party_edit_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate']


Party_list_columns = ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate']


Party_add_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Party_edit_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Party_show_field_set = [
    ('Data', {'fields': ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Partytype_add_columns = ['metadata', 'mindate', 'photo']


Partytype_edit_columns = ['metadata', 'mindate', 'photo']


Partytype_list_columns = ['metadata', 'mindate', 'photo']


Partytype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Partytype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Partytype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Payment_add_columns = ['amount', 'bill', 'bill1', 'date_paid', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated']


Payment_edit_columns = ['amount', 'bill', 'bill1', 'date_paid', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated']


Payment_list_columns = ['amount', 'bill', 'bill1', 'date_paid', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated']


Payment_add_field_set = [
    ('Data', {'fields': ['amount', 'bill', 'bill1', 'date_paid', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Payment_edit_field_set = [
    ('Data', {'fields': ['amount', 'bill', 'bill1', 'date_paid', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Payment_show_field_set = [
    ('Data', {'fields': ['amount', 'bill', 'bill1', 'date_paid', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffect_add_columns = ['metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo']


Personaleffect_edit_columns = ['metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo']


Personaleffect_list_columns = ['metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo']


Personaleffect_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffect_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffect_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffectscategory_add_columns = ['metadata', 'mindate', 'photo']


Personaleffectscategory_edit_columns = ['metadata', 'mindate', 'photo']


Personaleffectscategory_list_columns = ['metadata', 'mindate', 'photo']


Personaleffectscategory_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffectscategory_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Personaleffectscategory_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficer_add_columns = ['metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


Policeofficer_edit_columns = ['metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


Policeofficer_list_columns = ['metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']


Policeofficer_add_field_set = [
    ('Data', {'fields': ['metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficer_edit_field_set = [
    ('Data', {'fields': ['metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficer_show_field_set = [
    ('Data', {'fields': ['metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficerrank_add_columns = ['description', 'metadata', 'mindate', 'name', 'photo', 'sequence']


Policeofficerrank_edit_columns = ['description', 'metadata', 'mindate', 'name', 'photo', 'sequence']


Policeofficerrank_list_columns = ['description', 'metadata', 'mindate', 'name', 'photo', 'sequence']


Policeofficerrank_add_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo', 'sequence'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficerrank_edit_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo', 'sequence'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policeofficerrank_show_field_set = [
    ('Data', {'fields': ['description', 'metadata', 'mindate', 'name', 'photo', 'sequence'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestation_add_columns = ['metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']


Policestation_edit_columns = ['metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']


Policestation_list_columns = ['metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']


Policestation_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestation_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestation_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestationrank_add_columns = ['metadata', 'mindate', 'photo']


Policestationrank_edit_columns = ['metadata', 'mindate', 'photo']


Policestationrank_list_columns = ['metadata', 'mindate', 'photo']


Policestationrank_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestationrank_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Policestationrank_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prison_add_columns = ['metadata', 'mindate', 'photo', 'town', 'town1']


Prison_edit_columns = ['metadata', 'mindate', 'photo', 'town', 'town1']


Prison_list_columns = ['metadata', 'mindate', 'photo', 'town', 'town1']


Prison_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prison_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prison_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'town', 'town1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficer_add_columns = ['metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank']


Prisonofficer_edit_columns = ['metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank']


Prisonofficer_list_columns = ['metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank']


Prisonofficer_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficer_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficer_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficerrank_add_columns = ['metadata', 'mindate', 'photo']


Prisonofficerrank_edit_columns = ['metadata', 'mindate', 'photo']


Prisonofficerrank_list_columns = ['metadata', 'mindate', 'photo']


Prisonofficerrank_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficerrank_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prisonofficerrank_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutor_add_columns = ['lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam']


Prosecutor_edit_columns = ['lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam']


Prosecutor_list_columns = ['lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam']


Prosecutor_add_field_set = [
    ('Data', {'fields': ['lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutor_edit_field_set = [
    ('Data', {'fields': ['lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutor_show_field_set = [
    ('Data', {'fields': ['lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutorteam_add_columns = ['metadata', 'mindate', 'photo']


Prosecutorteam_edit_columns = ['metadata', 'mindate', 'photo']


Prosecutorteam_list_columns = ['metadata', 'mindate', 'photo']


Prosecutorteam_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutorteam_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Prosecutorteam_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Releasetype_add_columns = ['metadata', 'mindate', 'photo']


Releasetype_edit_columns = ['metadata', 'mindate', 'photo']


Releasetype_list_columns = ['metadata', 'mindate', 'photo']


Releasetype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Releasetype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Releasetype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Religion_add_columns = ['metadata', 'mindate', 'photo']


Religion_edit_columns = ['metadata', 'mindate', 'photo']


Religion_list_columns = ['metadata', 'mindate', 'photo']


Religion_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Religion_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Religion_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Schedulestatustype_add_columns = ['metadata', 'mindate', 'photo']


Schedulestatustype_edit_columns = ['metadata', 'mindate', 'photo']


Schedulestatustype_list_columns = ['metadata', 'mindate', 'photo']


Schedulestatustype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Schedulestatustype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Schedulestatustype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Seizure_add_columns = ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']


Seizure_edit_columns = ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']


Seizure_list_columns = ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']


Seizure_add_field_set = [
    ('Data', {'fields': ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Seizure_edit_field_set = [
    ('Data', {'fields': ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Seizure_show_field_set = [
    ('Data', {'fields': ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Settlement_add_columns = ['amount', 'complaint', 'complaint1', 'docx', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms']


Settlement_edit_columns = ['amount', 'complaint', 'complaint1', 'docx', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms']


Settlement_list_columns = ['amount', 'complaint', 'complaint1', 'docx', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms']


Settlement_add_field_set = [
    ('Data', {'fields': ['amount', 'complaint', 'complaint1', 'docx', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Settlement_edit_field_set = [
    ('Data', {'fields': ['amount', 'complaint', 'complaint1', 'docx', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Settlement_show_field_set = [
    ('Data', {'fields': ['amount', 'complaint', 'complaint1', 'docx', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Subcounty_add_columns = ['county', 'county1', 'metadata', 'mindate', 'photo']


Subcounty_edit_columns = ['county', 'county1', 'metadata', 'mindate', 'photo']


Subcounty_list_columns = ['county', 'county1', 'metadata', 'mindate', 'photo']


Subcounty_add_field_set = [
    ('Data', {'fields': ['county', 'county1', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Subcounty_edit_field_set = [
    ('Data', {'fields': ['county', 'county1', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Subcounty_show_field_set = [
    ('Data', {'fields': ['county', 'county1', 'metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Templatetype_add_columns = ['metadata', 'mindate', 'parent', 'photo', 'template_type']


Templatetype_edit_columns = ['metadata', 'mindate', 'parent', 'photo', 'template_type']


Templatetype_list_columns = ['metadata', 'mindate', 'parent', 'photo', 'template_type']


Templatetype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'parent', 'photo', 'template_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Templatetype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'parent', 'photo', 'template_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Templatetype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'parent', 'photo', 'template_type'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Town_add_columns = ['metadata', 'mindate', 'photo', 'ward']


Town_edit_columns = ['metadata', 'mindate', 'photo', 'ward']


Town_list_columns = ['metadata', 'mindate', 'photo', 'ward']


Town_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'ward'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Town_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'ward'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Town_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'ward'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Transcript_add_columns = ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'hearing', 'hearing1', 'locked', 'metadata', 'mindate', 'photo', 'video']


Transcript_edit_columns = ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'hearing', 'hearing1', 'locked', 'metadata', 'mindate', 'photo', 'video']


Transcript_list_columns = ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'hearing', 'hearing1', 'locked', 'metadata', 'mindate', 'photo', 'video']


Transcript_add_field_set = [
    ('Data', {'fields': ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'hearing', 'hearing1', 'locked', 'metadata', 'mindate', 'photo', 'video'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Transcript_edit_field_set = [
    ('Data', {'fields': ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'hearing', 'hearing1', 'locked', 'metadata', 'mindate', 'photo', 'video'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Transcript_show_field_set = [
    ('Data', {'fields': ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'hearing', 'hearing1', 'locked', 'metadata', 'mindate', 'photo', 'video'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Vehicle_add_columns = ['make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno']


Vehicle_edit_columns = ['make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno']


Vehicle_list_columns = ['make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno']


Vehicle_add_field_set = [
    ('Data', {'fields': ['make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Vehicle_edit_field_set = [
    ('Data', {'fields': ['make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Vehicle_show_field_set = [
    ('Data', {'fields': ['make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Ward_add_columns = ['metadata', 'mindate', 'photo', 'subcounty', 'subcounty1']


Ward_edit_columns = ['metadata', 'mindate', 'photo', 'subcounty', 'subcounty1']


Ward_list_columns = ['metadata', 'mindate', 'photo', 'subcounty', 'subcounty1']


Ward_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'subcounty', 'subcounty1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Ward_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'subcounty', 'subcounty1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Ward_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo', 'subcounty', 'subcounty1'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Warranttype_add_columns = ['metadata', 'mindate', 'photo']


Warranttype_edit_columns = ['metadata', 'mindate', 'photo']


Warranttype_list_columns = ['metadata', 'mindate', 'photo']


Warranttype_add_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Warranttype_edit_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]



Warranttype_show_field_set = [
    ('Data', {'fields': ['metadata', 'mindate', 'photo'], 'expanded': True}),
    ('Other', {'fields': ['file','photo','photo_img', 'photo_img_thumbnail'], 'expanded': False})
]


# exec("field_sets.py")



####################
# Table Views
####################
# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class AccounttypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Accounttype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Accounttype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Accounttype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Accounttype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Accounttype_add_field_set
    edit_fieldsets = Accounttype_edit_field_set
    show_fieldsets = Accounttype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['changed_by', 'changed_by_fk', 'changed_on', 'created_by', 'created_by_fk', 'created_on']

class AuditMixinView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(AuditMixin, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = AuditMixin_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = AuditMixin_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = AuditMixin_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  AuditMixin_add_field_set
    edit_fieldsets = AuditMixin_edit_field_set
    show_fieldsets = AuditMixin_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['assessing_registrar', 'bill_total', 'court', 'court1', 'court_account_account__types', 'court_account_courts', 'courtaccount', 'date_of_payment', 'document', 'documents', 'file', 'id', 'judicialofficer', 'judicialofficer1', 'lawyer', 'lawyer_paying', 'metadata', 'mindate', 'paid', 'party', 'party_paying', 'pay_code', 'photo', 'receiving_registrar', 'validated', 'validation_date']

class BillView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Bill, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Bill_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Bill_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Bill_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Bill_add_field_set
    edit_fieldsets = Bill_edit_field_set
    show_fieldsets = Bill_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['amount', 'feetype', 'feetype1', 'file', 'id', 'metadata', 'mindate', 'photo', 'purpose', 'qty', 'receipt', 'receipt_id', 'unit', 'unit_cost']

class BilldetailView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Billdetail, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Billdetail_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Billdetail_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Billdetail_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Billdetail_add_field_set
    edit_fieldsets = Billdetail_edit_field_set
    show_fieldsets = Billdetail_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['economic_class', 'economicclas', 'file', 'health_status', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'religion', 'religion1']

class BiodatumView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Biodatum, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Biodatum_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Biodatum_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Biodatum_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Biodatum_add_field_set
    edit_fieldsets = Biodatum_edit_field_set
    show_fieldsets = Biodatum_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['casechecklist', 'courtcase', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'subcategory']

class CasecategoryView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Casecategory, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Casecategory_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Casecategory_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Casecategory_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Casecategory_add_field_set
    edit_fieldsets = Casecategory_edit_field_set
    show_fieldsets = Casecategory_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'notes', 'photo']

class CasechecklistView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Casechecklist, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Casechecklist_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Casechecklist_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Casechecklist_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Casechecklist_add_field_set
    edit_fieldsets = Casechecklist_edit_field_set
    show_fieldsets = Casechecklist_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class CaselinktypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Caselinktype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Caselinktype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Caselinktype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Caselinktype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Caselinktype_add_field_set
    edit_fieldsets = Caselinktype_edit_field_set
    show_fieldsets = Caselinktype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class CelltypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Celltype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Celltype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Celltype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Celltype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Celltype_add_field_set
    edit_fieldsets = Celltype_edit_field_set
    show_fieldsets = Celltype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['arrest_date', 'arrival_date', 'casecomplete', 'cell_number', 'cell_type', 'celltype', 'commit_date', 'commital', 'commital_type', 'commitaltype', 'concurrent', 'court_case', 'courtcase', 'duration', 'exit_date', 'file', 'id', 'life_imprisonment', 'metadata', 'mindate', 'parent', 'parties', 'party', 'photo', 'police_station', 'policestation', 'prison', 'prisonofficer', 'prisonofficer1', 'prisons', 'purpose', 'reason_for_release', 'receiving_officer', 'release_date', 'release_type', 'releasetype', 'releasing_officer', 'remaining_days', 'remaining_months', 'remaining_years', 'sentence_start_date', 'warrant_date_attached', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_type', 'warranttype', 'with_children']

class CommitalView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Commital, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Commital_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Commital_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Commital_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Commital_add_field_set
    edit_fieldsets = Commital_edit_field_set
    show_fieldsets = Commital_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'maxduration', 'metadata', 'mindate', 'photo']

class CommitaltypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Commitaltype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Commitaltype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Commitaltype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Commitaltype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Commitaltype_add_field_set
    edit_fieldsets = Commitaltype_edit_field_set
    show_fieldsets = Commitaltype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaintcategory', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'daterecvd', 'evaluating_prosecutor_team', 'id', 'judicialofficer', 'magistrate_report_date', 'metadata', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'reported_to_judicial_officer', 'reportingofficer']

class ComplaintView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Complaint, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Complaint_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Complaint_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Complaint_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Complaint_add_field_set
    edit_fieldsets = Complaint_edit_field_set
    show_fieldsets = Complaint_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['complaint_category_parent', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo']

class ComplaintcategoryView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Complaintcategory, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Complaintcategory_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Complaintcategory_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Complaintcategory_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Complaintcategory_add_field_set
    edit_fieldsets = Complaintcategory_edit_field_set
    show_fieldsets = Complaintcategory_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class ComplaintroleView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Complaintrole, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Complaintrole_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Complaintrole_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Complaintrole_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Complaintrole_add_field_set
    edit_fieldsets = Complaintrole_edit_field_set
    show_fieldsets = Complaintrole_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'name', 'photo']

class CountryView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Country, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Country_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Country_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Country_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Country_add_field_set
    edit_fieldsets = Country_edit_field_set
    show_fieldsets = Country_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['country', 'country1', 'file', 'id', 'metadata', 'mindate', 'photo']

class CountyView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(County, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = County_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = County_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = County_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  County_add_field_set
    edit_fieldsets = County_edit_field_set
    show_fieldsets = County_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['court_rank', 'court_station', 'courtrank', 'courtstation', 'file', 'id', 'judicialofficer', 'metadata', 'mindate', 'photo', 'till_number', 'town', 'town1']

class CourtView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Court, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Court_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Court_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Court_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Court_add_field_set
    edit_fieldsets = Court_edit_field_set
    show_fieldsets = Court_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['account__types', 'account_name', 'account_number', 'accounttype', 'bank_name', 'court', 'courts', 'file', 'metadata', 'mindate', 'photo', 'short_code']

class CourtaccountView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Courtaccount, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Courtaccount_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Courtaccount_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Courtaccount_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Courtaccount_add_field_set
    edit_fieldsets = Courtaccount_edit_field_set
    show_fieldsets = Courtaccount_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['active', 'active_date', 'adr', 'appeal_number', 'appealed', 'award', 'case_admissible', 'case_filed_date', 'case_link_type', 'case_number', 'case_received_date', 'case_summary', 'caselinktype', 'combined_case', 'docket_number', 'fast_track', 'file', 'filing_prosecutor', 'govt_liability', 'grounds', 'id', 'indictment_date', 'interlocutory_judgement', 'inventory_of_docket', 'judgement', 'judgement_docx', 'judicialofficer', 'judicialofficer1', 'lawfirm', 'linked_cases', 'mediation_proposal', 'metadata', 'mindate', 'next_hearing_date', 'object_of_litigation', 'parent', 'photo', 'pretrial_date', 'pretrial_notes', 'pretrial_registrar', 'priority', 'prosecution_prayer', 'prosecutor', 'reopen', 'reopen_reason', 'value_in_dispute']

class CourtcaseView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Courtcase, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Courtcase_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Courtcase_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Courtcase_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Courtcase_add_field_set
    edit_fieldsets = Courtcase_edit_field_set
    show_fieldsets = Courtcase_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class CourtrankView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Courtrank, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Courtrank_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Courtrank_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Courtrank_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Courtrank_add_field_set
    edit_fieldsets = Courtrank_edit_field_set
    show_fieldsets = Courtrank_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'pay_bill', 'photo', 'till_number']

class CourtstationView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Courtstation, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Courtstation_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Courtstation_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Courtstation_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Courtstation_add_field_set
    edit_fieldsets = Courtstation_edit_field_set
    show_fieldsets = Courtstation_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['description', 'file', 'id', 'law', 'law1', 'metadata', 'mindate', 'photo', 'ref', 'ref_law']

class CrimeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Crime, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Crime_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Crime_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Crime_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Crime_add_field_set
    edit_fieldsets = Crime_edit_field_set
    show_fieldsets = Crime_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'investigationdiary', 'metadata', 'mindate', 'photo']

class CsiEquipmentView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(CsiEquipment, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = CsiEquipment_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = CsiEquipment_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = CsiEquipment_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  CsiEquipment_add_field_set
    edit_fieldsets = CsiEquipment_edit_field_set
    show_fieldsets = CsiEquipment_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['description', 'docx', 'file', 'id', 'image', 'investigation_diary', 'investigationdiary', 'metadata', 'mindate', 'photo']

class DiagramView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Diagram, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Diagram_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Diagram_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Diagram_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Diagram_add_field_set
    edit_fieldsets = Diagram_edit_field_set
    show_fieldsets = Diagram_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'photo', 'prison_officer', 'prisonofficer']

class DisciplineView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Discipline, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Discipline_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Discipline_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Discipline_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Discipline_add_field_set
    edit_fieldsets = Discipline_edit_field_set
    show_fieldsets = Discipline_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['docx', 'file', 'icon', 'id', 'metadata', 'mindate', 'name', 'photo', 'summary', 'template', 'template_type', 'templatetype', 'title']

class DoctemplateView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Doctemplate, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Doctemplate_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Doctemplate_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Doctemplate_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Doctemplate_add_field_set
    edit_fieldsets = Doctemplate_edit_field_set
    show_fieldsets = Doctemplate_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['admisibility_notes', 'admitted', 'citation', 'court_case', 'courtcase', 'doc_placed_by', 'doc_room', 'doc_row', 'doc_shelf', 'doc_template', 'doctemplate', 'document_admissibility', 'document_text', 'documenttype', 'docx', 'file', 'file_byte_count', 'file_create_date', 'file_ext', 'file_hash', 'file_load_path', 'file_parse_status', 'file_text', 'file_timestamp', 'file_update_date', 'file_upload_date', 'filing_date', 'id', 'is_scan', 'issue', 'issue1', 'judicial_officer', 'judicialofficer', 'metadata', 'mindate', 'name', 'page_count', 'paid', 'photo', 'publish_date', 'publish_newspaper', 'published', 'validated', 'visible']

class DocumentView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Document, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Document_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Document_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Document_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Document_add_field_set
    edit_fieldsets = Document_edit_field_set
    show_fieldsets = Document_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class DocumenttypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Documenttype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Documenttype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Documenttype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Documenttype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Documenttype_add_field_set
    edit_fieldsets = Documenttype_edit_field_set
    show_fieldsets = Documenttype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']

class EconomicclasView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Economicclas, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Economicclas_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Economicclas_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Economicclas_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Economicclas_add_field_set
    edit_fieldsets = Economicclas_edit_field_set
    show_fieldsets = Economicclas_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['docx', 'exhibit_no', 'file', 'id', 'investigation_entry', 'investigationdiary', 'metadata', 'mindate', 'photo', 'seizure', 'seizure1']

class ExhibitView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Exhibit, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Exhibit_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Exhibit_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Exhibit_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Exhibit_add_field_set
    edit_fieldsets = Exhibit_edit_field_set
    show_fieldsets = Exhibit_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['credentials', 'experttype', 'file', 'id', 'institution', 'jobtitle', 'metadata', 'mindate', 'photo']

class ExpertView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Expert, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Expert_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Expert_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Expert_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Expert_add_field_set
    edit_fieldsets = Expert_edit_field_set
    show_fieldsets = Expert_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['docx', 'expert', 'experts', 'file', 'investigating_officer', 'investigation_entries', 'investigationdiary', 'metadata', 'mindate', 'photo', 'requesting_officer', 'statement', 'summary_of_facts', 'task_given', 'task_request_date', 'testimony_date', 'validated']

class ExperttestimonyView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Experttestimony, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Experttestimony_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Experttestimony_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Experttestimony_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Experttestimony_add_field_set
    edit_fieldsets = Experttestimony_edit_field_set
    show_fieldsets = Experttestimony_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class ExperttypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Experttype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Experttype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Experttype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Experttype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Experttype_add_field_set
    edit_fieldsets = Experttype_edit_field_set
    show_fieldsets = Experttype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['fee_type', 'file', 'id', 'metadata', 'mindate', 'parent', 'photo']

class FeeclasView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Feeclas, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Feeclas_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Feeclas_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Feeclas_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Feeclas_add_field_set
    edit_fieldsets = Feeclas_edit_field_set
    show_fieldsets = Feeclas_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['account_type', 'accounttype', 'amount', 'description', 'feeclas', 'file', 'filing_fee_type', 'guide_clause', 'guide_sec', 'id', 'max_fee', 'metadata', 'min_fee', 'mindate', 'photo', 'unit']

class FeetypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Feetype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Feetype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Feetype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Feetype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Feetype_add_field_set
    edit_fieldsets = Feetype_edit_field_set
    show_fieldsets = Feetype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['dispatch', 'has_argument', 'is_server_default', 'reflected']

class FetchedValueView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(FetchedValue, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = FetchedValue_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = FetchedValue_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = FetchedValue_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  FetchedValue_add_field_set
    edit_fieldsets = FetchedValue_edit_field_set
    show_fieldsets = FetchedValue_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']

class FileColumnView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(FileColumn, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = FileColumn_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = FileColumn_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = FileColumn_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  FileColumn_add_field_set
    edit_fieldsets = FileColumn_edit_field_set
    show_fieldsets = FileColumn_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['enddate', 'file', 'health_event_type', 'healtheventtype', 'id', 'metadata', 'mindate', 'notes', 'party', 'party1', 'photo', 'prisonofficer', 'reporting_prison_officer', 'startdate']

class HealtheventView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Healthevent, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Healthevent_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Healthevent_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Healthevent_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Healthevent_add_field_set
    edit_fieldsets = Healthevent_edit_field_set
    show_fieldsets = Healthevent_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class HealtheventtypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Healtheventtype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Healtheventtype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Healtheventtype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Healtheventtype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Healtheventtype_add_field_set
    edit_fieldsets = Healtheventtype_edit_field_set
    show_fieldsets = Healtheventtype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['adjourned_to', 'adjournment_reason', 'atendance', 'completed', 'court_cases', 'courtcase', 'endtime', 'file', 'hearing_date', 'hearing_type', 'hearingtype', 'id', 'issue', 'judicialofficer', 'lawfirm', 'lawfirm1', 'metadata', 'mindate', 'next_hearing_date', 'notes', 'photo', 'postponement_reason', 'reason', 'schedule_status', 'schedulestatustype', 'sequence', 'starttime', 'transcript', 'yearday']

class HearingView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Hearing, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Hearing_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Hearing_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Hearing_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Hearing_add_field_set
    edit_fieldsets = Hearing_edit_field_set
    show_fieldsets = Hearing_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'hearing_type', 'id', 'metadata', 'mindate', 'parent', 'photo']

class HearingtypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Hearingtype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Hearingtype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Hearingtype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Hearingtype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Hearingtype_add_field_set
    edit_fieldsets = Hearingtype_edit_field_set
    show_fieldsets = Hearingtype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['coerce_to_is_types', 'comparator_factory', 'dispatch', 'hashable', 'python_type', 'should_evaluate_none']

class ImageColumnView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(ImageColumn, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = ImageColumn_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = ImageColumn_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = ImageColumn_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  ImageColumn_add_field_set
    edit_fieldsets = ImageColumn_edit_field_set
    show_fieldsets = ImageColumn_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['keep_image_formats']

class ImageManagerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(ImageManager, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = ImageManager_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = ImageManager_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = ImageManager_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  ImageManager_add_field_set
    edit_fieldsets = ImageManager_edit_field_set
    show_fieldsets = ImageManager_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['crime', 'crime_date', 'crime_detail', 'crimes', 'date_note', 'file', 'issue', 'metadata', 'mindate', 'parties', 'party', 'photo', 'place_note', 'place_of_crime', 'tffender_type']

class InstancecrimeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Instancecrime, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Instancecrime_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Instancecrime_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Instancecrime_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Instancecrime_add_field_set
    edit_fieldsets = Instancecrime_edit_field_set
    show_fieldsets = Instancecrime_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['answer', 'file', 'id', 'investigation_entry', 'investigationdiary', 'language', 'metadata', 'mindate', 'photo', 'question', 'validated']

class InterviewView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Interview, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Interview_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Interview_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Interview_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Interview_add_field_set
    edit_fieldsets = Interview_edit_field_set
    show_fieldsets = Interview_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['date_assigned', 'file', 'id', 'investigationdiary', 'lead_investigator', 'metadata', 'mindate', 'photo', 'police_officers', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']

class InvestigatingOfficerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(InvestigatingOfficer, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = InvestigatingOfficer_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = InvestigatingOfficer_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = InvestigatingOfficer_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  InvestigatingOfficer_add_field_set
    edit_fieldsets = InvestigatingOfficer_edit_field_set
    show_fieldsets = InvestigatingOfficer_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['activity', 'advocate_present', 'arrest_statement', 'arrest_warrant', 'complaint', 'complaint1', 'detained', 'detained_at', 'docx', 'enddate', 'equipmentresults', 'file', 'id', 'location', 'metadata', 'mindate', 'outcome', 'party', 'photo', 'provisional_release_statement', 'search_seizure_statement', 'startdate', 'summons_statement', 'vehicle', 'warrant_delivered_by', 'warrant_docx', 'warrant_issue_date', 'warrant_issued_by', 'warrant_received_by', 'warrant_serve_date', 'warrant_type', 'warrant_upload_date', 'warranttype']

class InvestigationdiaryView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Investigationdiary, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Investigationdiary_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Investigationdiary_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Investigationdiary_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Investigationdiary_add_field_set
    edit_fieldsets = Investigationdiary_edit_field_set
    show_fieldsets = Investigationdiary_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['argument', 'argument_date', 'argument_docx', 'counter_claim', 'court_case', 'courtcase', 'debt_amount', 'defense_lawyer', 'determination', 'determination_docx', 'dtermination_date', 'facts', 'file', 'hearing_date', 'id', 'is_criminal', 'issue', 'judicial_officer', 'judicialofficer', 'lawyer', 'lawyer1', 'legal_element', 'legalreference', 'legalreference1', 'material_element', 'metadata', 'mindate', 'moral_element', 'party', 'party1', 'photo', 'prosecutor', 'prosecutor1', 'rebuttal', 'rebuttal_date', 'rebuttal_docx', 'resolved', 'tasks']

class IssueView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Issue, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Issue_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Issue_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Issue_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Issue_add_field_set
    edit_fieldsets = Issue_edit_field_set
    show_fieldsets = Issue_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['court_station', 'courtstation', 'file', 'id', 'judicial_role', 'judicialrank', 'judicialrole', 'metadata', 'mindate', 'photo', 'rank']

class JudicialofficerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Judicialofficer, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Judicialofficer_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Judicialofficer_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Judicialofficer_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Judicialofficer_add_field_set
    edit_fieldsets = Judicialofficer_edit_field_set
    show_fieldsets = Judicialofficer_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class JudicialrankView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Judicialrank, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Judicialrank_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Judicialrank_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Judicialrank_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Judicialrank_add_field_set
    edit_fieldsets = Judicialrank_edit_field_set
    show_fieldsets = Judicialrank_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class JudicialroleView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Judicialrole, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Judicialrole_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Judicialrole_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Judicialrole_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Judicialrole_add_field_set
    edit_fieldsets = Judicialrole_edit_field_set
    show_fieldsets = Judicialrole_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']

class LawView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Law, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Law_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Law_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Law_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Law_add_field_set
    edit_fieldsets = Law_edit_field_set
    show_fieldsets = Law_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class LawfirmView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Lawfirm, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Lawfirm_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Lawfirm_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Lawfirm_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Lawfirm_add_field_set
    edit_fieldsets = Lawfirm_edit_field_set
    show_fieldsets = Lawfirm_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['bar_date', 'bar_no', 'file', 'id', 'law_firm', 'lawfirm', 'metadata', 'mindate', 'party', 'photo']

class LawyerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Lawyer, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Lawyer_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Lawyer_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Lawyer_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Lawyer_add_field_set
    edit_fieldsets = Lawyer_edit_field_set
    show_fieldsets = Lawyer_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['citation', 'commentary', 'file', 'id', 'interpretation', 'metadata', 'mindate', 'photo', 'public', 'quote', 'ref', 'validated', 'verbatim']

class LegalreferenceView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Legalreference, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Legalreference_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Legalreference_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Legalreference_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Legalreference_add_field_set
    edit_fieldsets = Legalreference_edit_field_set
    show_fieldsets = Legalreference_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: []

class MarkupView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Markup, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Markup_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Markup_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Markup_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Markup_add_field_set
    edit_fieldsets = Markup_edit_field_set
    show_fieldsets = Markup_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['bind', 'dispatch', 'info', 'quote', 'sorted_tables', 'tables']

class MetaDataView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(MetaData, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = MetaData_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = MetaData_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = MetaData_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  MetaData_add_field_set
    edit_fieldsets = MetaData_edit_field_set
    show_fieldsets = MetaData_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['metadata']

class ModelView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Model, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Model_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Model_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Model_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Model_add_field_set
    edit_fieldsets = Model_edit_field_set
    show_fieldsets = Model_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['biodata', 'biodatum', 'childunder4', 'file', 'id', 'metadata', 'mindate', 'photo']

class NextofkinView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Nextofkin, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Nextofkin_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Nextofkin_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Nextofkin_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Nextofkin_add_field_set
    edit_fieldsets = Nextofkin_edit_field_set
    show_fieldsets = Nextofkin_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['abandon', 'add_date', 'confirmation', 'contact', 'delivered', 'file', 'id', 'message', 'metadata', 'mindate', 'notification_register', 'notificationregister', 'photo', 'retries', 'retry_count', 'send_date', 'sent']

class NotificationView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Notification, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Notification_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Notification_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Notification_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Notification_add_field_set
    edit_fieldsets = Notification_edit_field_set
    show_fieldsets = Notification_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['active', 'complaint', 'complaint1', 'complaint_category', 'complaintcategory', 'contact', 'court_case', 'courtcase', 'document', 'document1', 'file', 'health_event', 'healthevent', 'hearing', 'hearing1', 'id', 'metadata', 'mindate', 'notification_type', 'notificationtype', 'notify_event', 'notifyevent', 'party', 'party1', 'photo', 'retry_count']

class NotificationregisterView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Notificationregister, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Notificationregister_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Notificationregister_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Notificationregister_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Notificationregister_add_field_set
    edit_fieldsets = Notificationregister_edit_field_set
    show_fieldsets = Notificationregister_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo']

class NotificationtypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Notificationtype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Notificationtype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Notificationtype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Notificationtype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Notificationtype_add_field_set
    edit_fieldsets = Notificationtype_edit_field_set
    show_fieldsets = Notificationtype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class NotifyeventView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Notifyevent, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Notifyevent_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Notifyevent_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Notifyevent_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Notifyevent_add_field_set
    edit_fieldsets = Notifyevent_edit_field_set
    show_fieldsets = Notifyevent_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['create_date', 'document', 'document1', 'file', 'id', 'image_ext', 'image_height', 'image_width', 'metadata', 'mindate', 'page_image', 'page_no', 'page_text', 'photo', 'update_date', 'upload_dt']

class PageView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Page, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Page_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Page_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Page_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Page_add_field_set
    edit_fieldsets = Page_edit_field_set
    show_fieldsets = Page_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['active', 'casefileinformation', 'casesummary', 'charge_sheet', 'charge_sheet_docx', 'circumstances', 'close_date', 'close_reason', 'closed', 'complaint_role', 'complaintcategory', 'complaintrole', 'complaints', 'complaintstatement', 'courtcase', 'datecaseopened', 'datefiled', 'dateofrepresentation', 'daterecvd', 'evaluating_prosecutor_team', 'file', 'id', 'is_infant', 'is_minor', 'judicialofficer', 'magistrate_report_date', 'metadata', 'mindate', 'miranda_date', 'miranda_read', 'miranda_witness', 'notes', 'ob_number', 'p_closed', 'p_evaluation', 'p_instruction', 'p_recommend_charge', 'p_request_help', 'p_submission_date', 'p_submission_notes', 'p_submitted', 'parent', 'party_type', 'partytype', 'photo', 'police_station', 'policeofficer', 'policestation', 'prosecutorteam', 'relationship_type', 'relative', 'reported_to_judicial_officer', 'reportingofficer', 'settlement', 'statement', 'statementdate']

class PartyView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Party, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Party_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Party_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Party_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Party_add_field_set
    edit_fieldsets = Party_edit_field_set
    show_fieldsets = Party_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class PartytypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Partytype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Partytype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Partytype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Partytype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Partytype_add_field_set
    edit_fieldsets = Partytype_edit_field_set
    show_fieldsets = Partytype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['amount', 'bill', 'bill1', 'date_paid', 'file', 'id', 'metadata', 'mindate', 'payment_description', 'payment_ref', 'phone_number', 'photo', 'validated']

class PaymentView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Payment, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Payment_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Payment_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Payment_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Payment_add_field_set
    edit_fieldsets = Payment_edit_field_set
    show_fieldsets = Payment_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'party', 'party1', 'personal_effects_category', 'personaleffectscategory', 'photo']

class PersonaleffectView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Personaleffect, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Personaleffect_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Personaleffect_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Personaleffect_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Personaleffect_add_field_set
    edit_fieldsets = Personaleffect_edit_field_set
    show_fieldsets = Personaleffect_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class PersonaleffectscategoryView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Personaleffectscategory, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Personaleffectscategory_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Personaleffectscategory_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Personaleffectscategory_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Personaleffectscategory_add_field_set
    edit_fieldsets = Personaleffectscategory_edit_field_set
    show_fieldsets = Personaleffectscategory_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['id', 'metadata', 'police_rank', 'policeofficerrank', 'policestation', 'servicenumber']

class PoliceofficerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Policeofficer, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Policeofficer_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Policeofficer_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Policeofficer_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Policeofficer_add_field_set
    edit_fieldsets = Policeofficer_edit_field_set
    show_fieldsets = Policeofficer_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['description', 'file', 'id', 'metadata', 'mindate', 'name', 'photo', 'sequence']

class PoliceofficerrankView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Policeofficerrank, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Policeofficerrank_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Policeofficerrank_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Policeofficerrank_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Policeofficerrank_add_field_set
    edit_fieldsets = Policeofficerrank_edit_field_set
    show_fieldsets = Policeofficerrank_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'officer_commanding', 'photo', 'police_station_rank', 'policeofficer', 'policestationrank', 'town', 'town1']

class PolicestationView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Policestation, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Policestation_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Policestation_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Policestation_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Policestation_add_field_set
    edit_fieldsets = Policestation_edit_field_set
    show_fieldsets = Policestation_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class PolicestationrankView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Policestationrank, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Policestationrank_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Policestationrank_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Policestationrank_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Policestationrank_add_field_set
    edit_fieldsets = Policestationrank_edit_field_set
    show_fieldsets = Policestationrank_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo', 'town', 'town1']

class PrisonView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Prison, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Prison_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Prison_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Prison_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Prison_add_field_set
    edit_fieldsets = Prison_edit_field_set
    show_fieldsets = Prison_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo', 'prison', 'prison1', 'prison_officer_rank', 'prisonofficerrank']

class PrisonofficerView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Prisonofficer, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Prisonofficer_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Prisonofficer_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Prisonofficer_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Prisonofficer_add_field_set
    edit_fieldsets = Prisonofficer_edit_field_set
    show_fieldsets = Prisonofficer_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class PrisonofficerrankView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Prisonofficerrank, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Prisonofficerrank_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Prisonofficerrank_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Prisonofficerrank_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Prisonofficerrank_add_field_set
    edit_fieldsets = Prisonofficerrank_edit_field_set
    show_fieldsets = Prisonofficerrank_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'lawyer', 'lawyer1', 'metadata', 'mindate', 'photo', 'prosecutor_team', 'prosecutorteam']

class ProsecutorView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Prosecutor, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Prosecutor_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Prosecutor_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Prosecutor_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Prosecutor_add_field_set
    edit_fieldsets = Prosecutor_edit_field_set
    show_fieldsets = Prosecutor_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class ProsecutorteamView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Prosecutorteam, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Prosecutorteam_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Prosecutorteam_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Prosecutorteam_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Prosecutorteam_add_field_set
    edit_fieldsets = Prosecutorteam_edit_field_set
    show_fieldsets = Prosecutorteam_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class ReleasetypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Releasetype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Releasetype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Releasetype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Releasetype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Releasetype_add_field_set
    edit_fieldsets = Releasetype_edit_field_set
    show_fieldsets = Releasetype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class ReligionView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Religion, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Religion_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Religion_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Religion_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Religion_add_field_set
    edit_fieldsets = Religion_edit_field_set
    show_fieldsets = Religion_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class SchedulestatustypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Schedulestatustype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Schedulestatustype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Schedulestatustype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Schedulestatustype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Schedulestatustype_add_field_set
    edit_fieldsets = Schedulestatustype_edit_field_set
    show_fieldsets = Schedulestatustype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['destroyed', 'destruction_date', 'destruction_notes', 'destruction_pic', 'destruction_witnesses', 'disposal_date', 'disposal_price', 'disposal_receipt', 'disposed', 'docx', 'file', 'id', 'immovable', 'investigation_diary', 'investigationdiary', 'is_evidence', 'item', 'item_description', 'item_packaging', 'item_pic', 'metadata', 'mindate', 'notes', 'owner', 'photo', 'premises', 'recovery_town', 'reg_no', 'return_date', 'return_notes', 'return_signed_receipt', 'returned', 'sold_to', 'town', 'witness']

class SeizureView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Seizure, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Seizure_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Seizure_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Seizure_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Seizure_add_field_set
    edit_fieldsets = Seizure_edit_field_set
    show_fieldsets = Seizure_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['amount', 'complaint', 'complaint1', 'docx', 'file', 'id', 'metadata', 'mindate', 'paid', 'party', 'photo', 'settlor', 'terms']

class SettlementView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Settlement, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Settlement_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Settlement_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Settlement_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Settlement_add_field_set
    edit_fieldsets = Settlement_edit_field_set
    show_fieldsets = Settlement_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['county', 'county1', 'file', 'id', 'metadata', 'mindate', 'photo']

class SubcountyView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Subcounty, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Subcounty_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Subcounty_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Subcounty_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Subcounty_add_field_set
    edit_fieldsets = Subcounty_edit_field_set
    show_fieldsets = Subcounty_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'parent', 'photo', 'template_type']

class TemplatetypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Templatetype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Templatetype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Templatetype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Templatetype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Templatetype_add_field_set
    edit_fieldsets = Templatetype_edit_field_set
    show_fieldsets = Templatetype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo', 'ward']

class TownView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Town, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Town_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Town_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Town_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Town_add_field_set
    edit_fieldsets = Town_edit_field_set
    show_fieldsets = Town_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['add_date', 'asr_date', 'asr_transcript', 'audio', 'certfiy_date', 'certified_transcript', 'edit_date', 'edited_transcript', 'file', 'hearing', 'hearing1', 'id', 'locked', 'metadata', 'mindate', 'photo', 'video']

class TranscriptView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Transcript, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Transcript_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Transcript_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Transcript_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Transcript_add_field_set
    edit_fieldsets = Transcript_edit_field_set
    show_fieldsets = Transcript_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'make', 'metadata', 'mindate', 'model', 'photo', 'police_station', 'policestation', 'regno']

class VehicleView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Vehicle, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Vehicle_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Vehicle_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Vehicle_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Vehicle_add_field_set
    edit_fieldsets = Vehicle_edit_field_set
    show_fieldsets = Vehicle_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo', 'subcounty', 'subcounty1']

class WardView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Ward, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Ward_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Ward_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Ward_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Ward_add_field_set
    edit_fieldsets = Ward_edit_field_set
    show_fieldsets = Ward_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    



# FIELDS: ['file', 'id', 'metadata', 'mindate', 'photo']

class WarranttypeView(ModelView):  # MasterDetailView, MultipleView, CompactCRUDMixin
    datamodel = SQLAInterface(Warranttype, db.session)

    # add_title =
    # related_views =[]
    # list_title =
    # edit_title =
    # show_title =
    # add_widget = (FormVerticalWidget|FormInlineWidget)
    # show_widget = ShowBlockWidget
    # list_widget = (ListThumbnail|ListWidget|ListItem|ListBlock)
    # base_order = ("name", "asc")
    # base_filters = [[created_by, FilterEqualFunction, get_user]] #[name, FilterStartsWith, a]],
    # search_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns
    search_exclude_columns = ['file', 'photo', 'photo_img', 'photo_img_thumbnail'] #+ person_exclude_columns + biometric_columns + person_search_exclude_columns
    # search_form_query_rel_fields = [(group:[[name,FilterStartsWith,W]]
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns
    # label_columns = {"contact_group":"Contacts Group"}
    # add_columns = person_list_columns + ref_columns + contact_columns
    add_columns = Warranttype_add_columns
    # edit_columns = person_list_columns + ref_columns + contact_columns
    edit_columns = Warranttype_edit_columns
    # list_columns = person_list_columns + ref_columns + contact_columns
    list_columns = Warranttype_list_columns
    # list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
    # page_size = 10
    # formatters_columns = {‘some_date_col’: lambda x: x.isoformat() }
    # show_fieldsets = person_show_fieldset + contact_fieldset
    # edit_fieldsets = add_fieldsets =     #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    add_fieldsets =  Warranttype_add_field_set
    edit_fieldsets = Warranttype_edit_field_set
    show_fieldsets = Warranttype_show_field_set
    #     # ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset
    # description_columns = {"name":"your models name column","address":"the address column"}
    # base_permissions = ['can_add', 'can_edit', 'can_delete', 'can_list', 'can_show', 'can_download']
    #
    # show_template = "appbuilder/general/model/show_cascade.html"
    # edit_template = "appbuilder/general/model/edit_cascade.html"
    
    # validators_columns = {'my_field1': [EqualTo('my_field2',
    #                                              message=gettext('fields must match'))
    #                                      ]
    #                        }
    #
    # add_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # edit_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    # search_form_query_rel_fields = {'group': [['name',FilterStartsWith,'W']] }
    
    # @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    # def myaction(self, item):
    #     # Do domething with this record
    #     return redirect(self.get_redirect())
    
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())
    






####################
# Join Table Views
####################
# View Table for:t_casecategory_courtcase

class t_casecategory_courtcaseView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_casecategory_courtcase)
    # list_columns = []




# View Table for:t_casecategorychecklist

class t_casecategorychecklistView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_casecategorychecklist)
    # list_columns = []




# View Table for:t_complaint_complaintcategory

class t_complaint_complaintcategoryView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_complaint_complaintcategory)
    # list_columns = []




# View Table for:t_complaint_courtcase

class t_complaint_courtcaseView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_complaint_courtcase)
    # list_columns = []




# View Table for:t_court_judicialofficer

class t_court_judicialofficerView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_court_judicialofficer)
    # list_columns = []




# View Table for:t_courtcase_judicialofficer

class t_courtcase_judicialofficerView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_courtcase_judicialofficer)
    # list_columns = []




# View Table for:t_courtcase_lawfirm

class t_courtcase_lawfirmView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_courtcase_lawfirm)
    # list_columns = []




# View Table for:t_csi_equipment_investigationdiary

class t_csi_equipment_investigationdiaryView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_csi_equipment_investigationdiary)
    # list_columns = []




# View Table for:t_document_documenttype

class t_document_documenttypeView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_document_documenttype)
    # list_columns = []




# View Table for:t_expert_experttype

class t_expert_experttypeView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_expert_experttype)
    # list_columns = []




# View Table for:t_hearing_issue

class t_hearing_issueView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_hearing_issue)
    # list_columns = []




# View Table for:t_hearing_judicialofficer

class t_hearing_judicialofficerView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_hearing_judicialofficer)
    # list_columns = []




# View Table for:t_hearing_lawfirm

class t_hearing_lawfirmView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_hearing_lawfirm)
    # list_columns = []




# View Table for:t_hearing_lawfirm_2

class t_hearing_lawfirm_2View(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_hearing_lawfirm_2)
    # list_columns = []




# View Table for:t_instancecrime_issue

class t_instancecrime_issueView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_instancecrime_issue)
    # list_columns = []




# View Table for:t_investigating_officer_investigationdiary

class t_investigating_officer_investigationdiaryView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_investigating_officer_investigationdiary)
    # list_columns = []




# View Table for:t_investigationdiary_party

class t_investigationdiary_partyView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_investigationdiary_party)
    # list_columns = []




# View Table for:t_investigationdiary_vehicle

class t_investigationdiary_vehicleView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_investigationdiary_vehicle)
    # list_columns = []




# View Table for:t_issue_lawyer

class t_issue_lawyerView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_issue_lawyer)
    # list_columns = []




# View Table for:t_issue_legalreference

class t_issue_legalreferenceView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_issue_legalreference)
    # list_columns = []




# View Table for:t_issue_legalreference_2

class t_issue_legalreference_2View(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_issue_legalreference_2)
    # list_columns = []




# View Table for:t_issue_party

class t_issue_partyView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_issue_party)
    # list_columns = []




# View Table for:t_issue_party_2

class t_issue_party_2View(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_issue_party_2)
    # list_columns = []




# View Table for:t_lawyer_party

class t_lawyer_partyView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_lawyer_party)
    # list_columns = []




# View Table for:t_party_settlement

class t_party_settlementView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_party_settlement)
    # list_columns = []




# View Table for:t_policeofficer_policestation

class t_policeofficer_policestationView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_policeofficer_policestation)
    # list_columns = []




# View Table for:t_town_ward

class t_town_wardView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(t_town_ward)
    # list_columns = []







####################
# Join MultipleViews
####################

# MultiView for:t_casecategory_courtcase

class t_casecategory_courtcaseMultiView(MultipleView):
    

	views = ['CasecategoryView', 'CourtcaseView']





# MultiView for:t_casecategorychecklist

class t_casecategorychecklistMultiView(MultipleView):
    

	views = ['CasecategorychecklistView']





# MultiView for:t_complaint_complaintcategory

class t_complaint_complaintcategoryMultiView(MultipleView):
    

	views = ['ComplaintView', 'ComplaintcategoryView']





# MultiView for:t_complaint_courtcase

class t_complaint_courtcaseMultiView(MultipleView):
    

	views = ['ComplaintView', 'CourtcaseView']





# MultiView for:t_court_judicialofficer

class t_court_judicialofficerMultiView(MultipleView):
    

	views = ['CourtView', 'JudicialofficerView']





# MultiView for:t_courtcase_judicialofficer

class t_courtcase_judicialofficerMultiView(MultipleView):
    

	views = ['CourtcaseView', 'JudicialofficerView']





# MultiView for:t_courtcase_lawfirm

class t_courtcase_lawfirmMultiView(MultipleView):
    

	views = ['CourtcaseView', 'LawfirmView']





# MultiView for:t_csi_equipment_investigationdiary

class t_csi_equipment_investigationdiaryMultiView(MultipleView):
    

	views = ['CsiView', 'EquipmentView', 'InvestigationdiaryView']





# MultiView for:t_document_documenttype

class t_document_documenttypeMultiView(MultipleView):
    

	views = ['DocumentView', 'DocumenttypeView']





# MultiView for:t_expert_experttype

class t_expert_experttypeMultiView(MultipleView):
    

	views = ['ExpertView', 'ExperttypeView']





# MultiView for:t_hearing_issue

class t_hearing_issueMultiView(MultipleView):
    

	views = ['HearingView', 'IssueView']





# MultiView for:t_hearing_judicialofficer

class t_hearing_judicialofficerMultiView(MultipleView):
    

	views = ['HearingView', 'JudicialofficerView']





# MultiView for:t_hearing_lawfirm

class t_hearing_lawfirmMultiView(MultipleView):
    

	views = ['HearingView', 'LawfirmView']





# MultiView for:t_hearing_lawfirm_2

class t_hearing_lawfirm_2MultiView(MultipleView):
    

	views = ['HearingView', 'LawfirmView', '2View']





# MultiView for:t_instancecrime_issue

class t_instancecrime_issueMultiView(MultipleView):
    

	views = ['InstancecrimeView', 'IssueView']





# MultiView for:t_investigating_officer_investigationdiary

class t_investigating_officer_investigationdiaryMultiView(MultipleView):
    

	views = ['InvestigatingView', 'OfficerView', 'InvestigationdiaryView']





# MultiView for:t_investigationdiary_party

class t_investigationdiary_partyMultiView(MultipleView):
    

	views = ['InvestigationdiaryView', 'PartyView']





# MultiView for:t_investigationdiary_vehicle

class t_investigationdiary_vehicleMultiView(MultipleView):
    

	views = ['InvestigationdiaryView', 'VehicleView']





# MultiView for:t_issue_lawyer

class t_issue_lawyerMultiView(MultipleView):
    

	views = ['IssueView', 'LawyerView']





# MultiView for:t_issue_legalreference

class t_issue_legalreferenceMultiView(MultipleView):
    

	views = ['IssueView', 'LegalreferenceView']





# MultiView for:t_issue_legalreference_2

class t_issue_legalreference_2MultiView(MultipleView):
    

	views = ['IssueView', 'LegalreferenceView', '2View']





# MultiView for:t_issue_party

class t_issue_partyMultiView(MultipleView):
    

	views = ['IssueView', 'PartyView']





# MultiView for:t_issue_party_2

class t_issue_party_2MultiView(MultipleView):
    

	views = ['IssueView', 'PartyView', '2View']





# MultiView for:t_lawyer_party

class t_lawyer_partyMultiView(MultipleView):
    

	views = ['LawyerView', 'PartyView']





# MultiView for:t_party_settlement

class t_party_settlementMultiView(MultipleView):
    

	views = ['PartyView', 'SettlementView']





# MultiView for:t_policeofficer_policestation

class t_policeofficer_policestationMultiView(MultipleView):
    

	views = ['PoliceofficerView', 'PolicestationView']





# MultiView for:t_town_ward

class t_town_wardMultiView(MultipleView):
    

	views = ['TownView', 'WardView']







####################
# Chart Views
####################

class AccounttypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Accounttype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = AccounttypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class AuditMixinChartView(GroupByChartView):
    datamodel = SQLAInterface(AuditMixin, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = AuditMixinView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class BillChartView(GroupByChartView):
    datamodel = SQLAInterface(Bill, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = BillView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class BilldetailChartView(GroupByChartView):
    datamodel = SQLAInterface(Billdetail, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = BilldetailView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class BiodatumChartView(GroupByChartView):
    datamodel = SQLAInterface(Biodatum, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = BiodatumView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CasecategoryChartView(GroupByChartView):
    datamodel = SQLAInterface(Casecategory, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CasecategoryView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CasechecklistChartView(GroupByChartView):
    datamodel = SQLAInterface(Casechecklist, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CasechecklistView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CaselinktypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Caselinktype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CaselinktypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CelltypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Celltype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CelltypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CommitalChartView(GroupByChartView):
    datamodel = SQLAInterface(Commital, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CommitalView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CommitaltypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Commitaltype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CommitaltypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ComplaintChartView(GroupByChartView):
    datamodel = SQLAInterface(Complaint, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ComplaintView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ComplaintcategoryChartView(GroupByChartView):
    datamodel = SQLAInterface(Complaintcategory, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ComplaintcategoryView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ComplaintroleChartView(GroupByChartView):
    datamodel = SQLAInterface(Complaintrole, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ComplaintroleView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CountryChartView(GroupByChartView):
    datamodel = SQLAInterface(Country, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CountryView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CountyChartView(GroupByChartView):
    datamodel = SQLAInterface(County, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CountyView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CourtChartView(GroupByChartView):
    datamodel = SQLAInterface(Court, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CourtView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CourtaccountChartView(GroupByChartView):
    datamodel = SQLAInterface(Courtaccount, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CourtaccountView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CourtcaseChartView(GroupByChartView):
    datamodel = SQLAInterface(Courtcase, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CourtcaseView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CourtrankChartView(GroupByChartView):
    datamodel = SQLAInterface(Courtrank, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CourtrankView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CourtstationChartView(GroupByChartView):
    datamodel = SQLAInterface(Courtstation, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CourtstationView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CrimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Crime, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CrimeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class CsiEquipmentChartView(GroupByChartView):
    datamodel = SQLAInterface(CsiEquipment, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CsiEquipmentView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class DiagramChartView(GroupByChartView):
    datamodel = SQLAInterface(Diagram, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DiagramView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class DisciplineChartView(GroupByChartView):
    datamodel = SQLAInterface(Discipline, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DisciplineView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class DoctemplateChartView(GroupByChartView):
    datamodel = SQLAInterface(Doctemplate, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DoctemplateView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class DocumentChartView(GroupByChartView):
    datamodel = SQLAInterface(Document, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DocumentView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class DocumenttypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Documenttype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DocumenttypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class EconomicclasChartView(GroupByChartView):
    datamodel = SQLAInterface(Economicclas, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = EconomicclasView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ExhibitChartView(GroupByChartView):
    datamodel = SQLAInterface(Exhibit, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ExhibitView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ExpertChartView(GroupByChartView):
    datamodel = SQLAInterface(Expert, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ExpertView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ExperttestimonyChartView(GroupByChartView):
    datamodel = SQLAInterface(Experttestimony, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ExperttestimonyView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ExperttypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Experttype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ExperttypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class FeeclasChartView(GroupByChartView):
    datamodel = SQLAInterface(Feeclas, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = FeeclasView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class FeetypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Feetype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = FeetypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class FetchedValueChartView(GroupByChartView):
    datamodel = SQLAInterface(FetchedValue, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = FetchedValueView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class FileColumnChartView(GroupByChartView):
    datamodel = SQLAInterface(FileColumn, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = FileColumnView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class HealtheventChartView(GroupByChartView):
    datamodel = SQLAInterface(Healthevent, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = HealtheventView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class HealtheventtypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Healtheventtype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = HealtheventtypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class HearingChartView(GroupByChartView):
    datamodel = SQLAInterface(Hearing, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = HearingView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class HearingtypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Hearingtype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = HearingtypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ImageColumnChartView(GroupByChartView):
    datamodel = SQLAInterface(ImageColumn, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ImageColumnView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ImageManagerChartView(GroupByChartView):
    datamodel = SQLAInterface(ImageManager, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ImageManagerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class InstancecrimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Instancecrime, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = InstancecrimeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class InterviewChartView(GroupByChartView):
    datamodel = SQLAInterface(Interview, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = InterviewView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class InvestigatingOfficerChartView(GroupByChartView):
    datamodel = SQLAInterface(InvestigatingOfficer, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = InvestigatingOfficerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class InvestigationdiaryChartView(GroupByChartView):
    datamodel = SQLAInterface(Investigationdiary, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = InvestigationdiaryView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class IssueChartView(GroupByChartView):
    datamodel = SQLAInterface(Issue, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = IssueView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class JudicialofficerChartView(GroupByChartView):
    datamodel = SQLAInterface(Judicialofficer, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = JudicialofficerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class JudicialrankChartView(GroupByChartView):
    datamodel = SQLAInterface(Judicialrank, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = JudicialrankView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class JudicialroleChartView(GroupByChartView):
    datamodel = SQLAInterface(Judicialrole, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = JudicialroleView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class LawChartView(GroupByChartView):
    datamodel = SQLAInterface(Law, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = LawView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class LawfirmChartView(GroupByChartView):
    datamodel = SQLAInterface(Lawfirm, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = LawfirmView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class LawyerChartView(GroupByChartView):
    datamodel = SQLAInterface(Lawyer, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = LawyerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class LegalreferenceChartView(GroupByChartView):
    datamodel = SQLAInterface(Legalreference, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = LegalreferenceView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class MarkupChartView(GroupByChartView):
    datamodel = SQLAInterface(Markup, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = MarkupView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class MetaDataChartView(GroupByChartView):
    datamodel = SQLAInterface(MetaData, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = MetaDataView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ModelChartView(GroupByChartView):
    datamodel = SQLAInterface(Model, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ModelView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class NextofkinChartView(GroupByChartView):
    datamodel = SQLAInterface(Nextofkin, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = NextofkinView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class NotificationChartView(GroupByChartView):
    datamodel = SQLAInterface(Notification, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = NotificationView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class NotificationregisterChartView(GroupByChartView):
    datamodel = SQLAInterface(Notificationregister, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = NotificationregisterView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class NotificationtypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Notificationtype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = NotificationtypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class NotifyeventChartView(GroupByChartView):
    datamodel = SQLAInterface(Notifyevent, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = NotifyeventView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PageChartView(GroupByChartView):
    datamodel = SQLAInterface(Page, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PageView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PartyChartView(GroupByChartView):
    datamodel = SQLAInterface(Party, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PartyView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PartytypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Partytype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PartytypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PaymentChartView(GroupByChartView):
    datamodel = SQLAInterface(Payment, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PaymentView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PersonaleffectChartView(GroupByChartView):
    datamodel = SQLAInterface(Personaleffect, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PersonaleffectView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PersonaleffectscategoryChartView(GroupByChartView):
    datamodel = SQLAInterface(Personaleffectscategory, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PersonaleffectscategoryView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PoliceofficerChartView(GroupByChartView):
    datamodel = SQLAInterface(Policeofficer, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PoliceofficerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PoliceofficerrankChartView(GroupByChartView):
    datamodel = SQLAInterface(Policeofficerrank, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PoliceofficerrankView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PolicestationChartView(GroupByChartView):
    datamodel = SQLAInterface(Policestation, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PolicestationView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PolicestationrankChartView(GroupByChartView):
    datamodel = SQLAInterface(Policestationrank, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PolicestationrankView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PrisonChartView(GroupByChartView):
    datamodel = SQLAInterface(Prison, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PrisonView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PrisonofficerChartView(GroupByChartView):
    datamodel = SQLAInterface(Prisonofficer, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PrisonofficerView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class PrisonofficerrankChartView(GroupByChartView):
    datamodel = SQLAInterface(Prisonofficerrank, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PrisonofficerrankView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ProsecutorChartView(GroupByChartView):
    datamodel = SQLAInterface(Prosecutor, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ProsecutorView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ProsecutorteamChartView(GroupByChartView):
    datamodel = SQLAInterface(Prosecutorteam, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ProsecutorteamView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ReleasetypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Releasetype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ReleasetypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class ReligionChartView(GroupByChartView):
    datamodel = SQLAInterface(Religion, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ReligionView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class SchedulestatustypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Schedulestatustype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = SchedulestatustypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class SeizureChartView(GroupByChartView):
    datamodel = SQLAInterface(Seizure, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = SeizureView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class SettlementChartView(GroupByChartView):
    datamodel = SQLAInterface(Settlement, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = SettlementView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class SubcountyChartView(GroupByChartView):
    datamodel = SQLAInterface(Subcounty, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = SubcountyView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class TemplatetypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Templatetype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = TemplatetypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class TownChartView(GroupByChartView):
    datamodel = SQLAInterface(Town, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = TownView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class TranscriptChartView(GroupByChartView):
    datamodel = SQLAInterface(Transcript, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = TranscriptView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class VehicleChartView(GroupByChartView):
    datamodel = SQLAInterface(Vehicle, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = VehicleView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class WardChartView(GroupByChartView):
    datamodel = SQLAInterface(Ward, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = WardView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    





class WarranttypeChartView(GroupByChartView):
    datamodel = SQLAInterface(Warranttype, db.session) 

    chart_title = 'Grouped Birthdays'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = WarranttypeView.label_columns
    # group_by_columns = ['birthday']
    definitions = [
        {
            "group": "age_today",
            'formatter': pretty_month_year,
            "series": [ (aggregate_count,"age_today"),
                        (aggregate_avg, 'population'),
                        (aggregate_avg, 'college')
                       ]
        },
        {
            'group': 'month_year',
            'formatter': pretty_month_year,
            'series': [(aggregate_sum, 'unemployed'),
                       (aggregate_avg, 'population'),
                       (aggregate_avg, 'college')
            ]
        }
    ]
    







####################
# WTForms-Alchemy Forms
####################



####################
# Just in case we ever need them
####################

class wtf_AccounttypeForm(ModelForm):
    class Meta:
        model = Accounttype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_AuditMixinForm(ModelForm):
    class Meta:
        model = AuditMixin
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_BillForm(ModelForm):
    class Meta:
        model = Bill
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_BilldetailForm(ModelForm):
    class Meta:
        model = Billdetail
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_BiodatumForm(ModelForm):
    class Meta:
        model = Biodatum
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CasecategoryForm(ModelForm):
    class Meta:
        model = Casecategory
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CasechecklistForm(ModelForm):
    class Meta:
        model = Casechecklist
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CaselinktypeForm(ModelForm):
    class Meta:
        model = Caselinktype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CelltypeForm(ModelForm):
    class Meta:
        model = Celltype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CommitalForm(ModelForm):
    class Meta:
        model = Commital
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CommitaltypeForm(ModelForm):
    class Meta:
        model = Commitaltype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ComplaintcategoryForm(ModelForm):
    class Meta:
        model = Complaintcategory
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ComplaintroleForm(ModelForm):
    class Meta:
        model = Complaintrole
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CountryForm(ModelForm):
    class Meta:
        model = Country
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CountyForm(ModelForm):
    class Meta:
        model = County
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CourtForm(ModelForm):
    class Meta:
        model = Court
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CourtaccountForm(ModelForm):
    class Meta:
        model = Courtaccount
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CourtcaseForm(ModelForm):
    class Meta:
        model = Courtcase
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CourtrankForm(ModelForm):
    class Meta:
        model = Courtrank
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CourtstationForm(ModelForm):
    class Meta:
        model = Courtstation
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CrimeForm(ModelForm):
    class Meta:
        model = Crime
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_CsiEquipmentForm(ModelForm):
    class Meta:
        model = CsiEquipment
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_DiagramForm(ModelForm):
    class Meta:
        model = Diagram
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_DisciplineForm(ModelForm):
    class Meta:
        model = Discipline
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_DoctemplateForm(ModelForm):
    class Meta:
        model = Doctemplate
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_DocumentForm(ModelForm):
    class Meta:
        model = Document
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_DocumenttypeForm(ModelForm):
    class Meta:
        model = Documenttype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_EconomicclasForm(ModelForm):
    class Meta:
        model = Economicclas
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ExhibitForm(ModelForm):
    class Meta:
        model = Exhibit
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ExpertForm(ModelForm):
    class Meta:
        model = Expert
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ExperttestimonyForm(ModelForm):
    class Meta:
        model = Experttestimony
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ExperttypeForm(ModelForm):
    class Meta:
        model = Experttype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_FeeclasForm(ModelForm):
    class Meta:
        model = Feeclas
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_FeetypeForm(ModelForm):
    class Meta:
        model = Feetype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_FetchedValueForm(ModelForm):
    class Meta:
        model = FetchedValue
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_FileColumnForm(ModelForm):
    class Meta:
        model = FileColumn
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_HealtheventForm(ModelForm):
    class Meta:
        model = Healthevent
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_HealtheventtypeForm(ModelForm):
    class Meta:
        model = Healtheventtype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_HearingForm(ModelForm):
    class Meta:
        model = Hearing
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_HearingtypeForm(ModelForm):
    class Meta:
        model = Hearingtype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ImageColumnForm(ModelForm):
    class Meta:
        model = ImageColumn
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ImageManagerForm(ModelForm):
    class Meta:
        model = ImageManager
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_InstancecrimeForm(ModelForm):
    class Meta:
        model = Instancecrime
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_InterviewForm(ModelForm):
    class Meta:
        model = Interview
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_InvestigatingOfficerForm(ModelForm):
    class Meta:
        model = InvestigatingOfficer
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_InvestigationdiaryForm(ModelForm):
    class Meta:
        model = Investigationdiary
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_IssueForm(ModelForm):
    class Meta:
        model = Issue
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_JudicialofficerForm(ModelForm):
    class Meta:
        model = Judicialofficer
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_JudicialrankForm(ModelForm):
    class Meta:
        model = Judicialrank
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_JudicialroleForm(ModelForm):
    class Meta:
        model = Judicialrole
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_LawForm(ModelForm):
    class Meta:
        model = Law
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_LawfirmForm(ModelForm):
    class Meta:
        model = Lawfirm
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_LawyerForm(ModelForm):
    class Meta:
        model = Lawyer
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_LegalreferenceForm(ModelForm):
    class Meta:
        model = Legalreference
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_MarkupForm(ModelForm):
    class Meta:
        model = Markup
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_MetaDataForm(ModelForm):
    class Meta:
        model = MetaData
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ModelForm(ModelForm):
    class Meta:
        model = Model
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_NextofkinForm(ModelForm):
    class Meta:
        model = Nextofkin
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_NotificationForm(ModelForm):
    class Meta:
        model = Notification
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_NotificationregisterForm(ModelForm):
    class Meta:
        model = Notificationregister
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_NotificationtypeForm(ModelForm):
    class Meta:
        model = Notificationtype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_NotifyeventForm(ModelForm):
    class Meta:
        model = Notifyevent
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PageForm(ModelForm):
    class Meta:
        model = Page
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PartyForm(ModelForm):
    class Meta:
        model = Party
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PartytypeForm(ModelForm):
    class Meta:
        model = Partytype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PaymentForm(ModelForm):
    class Meta:
        model = Payment
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PersonaleffectForm(ModelForm):
    class Meta:
        model = Personaleffect
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PersonaleffectscategoryForm(ModelForm):
    class Meta:
        model = Personaleffectscategory
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PoliceofficerForm(ModelForm):
    class Meta:
        model = Policeofficer
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PoliceofficerrankForm(ModelForm):
    class Meta:
        model = Policeofficerrank
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PolicestationForm(ModelForm):
    class Meta:
        model = Policestation
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PolicestationrankForm(ModelForm):
    class Meta:
        model = Policestationrank
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PrisonForm(ModelForm):
    class Meta:
        model = Prison
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PrisonofficerForm(ModelForm):
    class Meta:
        model = Prisonofficer
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_PrisonofficerrankForm(ModelForm):
    class Meta:
        model = Prisonofficerrank
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ProsecutorForm(ModelForm):
    class Meta:
        model = Prosecutor
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ProsecutorteamForm(ModelForm):
    class Meta:
        model = Prosecutorteam
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ReleasetypeForm(ModelForm):
    class Meta:
        model = Releasetype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_ReligionForm(ModelForm):
    class Meta:
        model = Religion
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_SchedulestatustypeForm(ModelForm):
    class Meta:
        model = Schedulestatustype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_SeizureForm(ModelForm):
    class Meta:
        model = Seizure
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_SettlementForm(ModelForm):
    class Meta:
        model = Settlement
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_SubcountyForm(ModelForm):
    class Meta:
        model = Subcounty
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_TemplatetypeForm(ModelForm):
    class Meta:
        model = Templatetype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_TownForm(ModelForm):
    class Meta:
        model = Town
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_TranscriptForm(ModelForm):
    class Meta:
        model = Transcript
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_WardForm(ModelForm):
    class Meta:
        model = Ward
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)





class wtf_WarranttypeForm(ModelForm):
    class Meta:
        model = Warranttype
        # include = ['author_id']
        # exclude = ['description']
        # only = ['name', 'content']
        # include_primary_keys = True
#         only_indexed_fields = True
#         strip_string_fields = True
#     location = ModelFormField(LocationForm)










####################
# View Registrations
####################
appbuilder.add_view(AccounttypeView(), "Accounttype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(AuditMixinView(), "AuditMixin", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(BillView(), "Bill", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(BilldetailView(), "Billdetail", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(BiodatumView(), "Biodatum", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CasecategoryView(), "Casecategory", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CasechecklistView(), "Casechecklist", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CaselinktypeView(), "Caselinktype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CelltypeView(), "Celltype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CommitalView(), "Commital", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CommitaltypeView(), "Commitaltype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ComplaintView(), "Complaint", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ComplaintcategoryView(), "Complaintcategory", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ComplaintroleView(), "Complaintrole", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CountryView(), "Country", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CountyView(), "County", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CourtView(), "Court", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CourtaccountView(), "Courtaccount", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CourtcaseView(), "Courtcase", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CourtrankView(), "Courtrank", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CourtstationView(), "Courtstation", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CrimeView(), "Crime", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CsiEquipmentView(), "CsiEquipment", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(DiagramView(), "Diagram", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(DisciplineView(), "Discipline", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(DoctemplateView(), "Doctemplate", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(DocumentView(), "Document", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(DocumenttypeView(), "Documenttype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(EconomicclasView(), "Economicclas", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ExhibitView(), "Exhibit", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ExpertView(), "Expert", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ExperttestimonyView(), "Experttestimony", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ExperttypeView(), "Experttype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(FeeclasView(), "Feeclas", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(FeetypeView(), "Feetype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(FetchedValueView(), "FetchedValue", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(FileColumnView(), "FileColumn", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(HealtheventView(), "Healthevent", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(HealtheventtypeView(), "Healtheventtype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(HearingView(), "Hearing", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(HearingtypeView(), "Hearingtype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ImageColumnView(), "ImageColumn", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ImageManagerView(), "ImageManager", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(InstancecrimeView(), "Instancecrime", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(InterviewView(), "Interview", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(InvestigatingOfficerView(), "InvestigatingOfficer", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(InvestigationdiaryView(), "Investigationdiary", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(IssueView(), "Issue", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(JudicialofficerView(), "Judicialofficer", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(JudicialrankView(), "Judicialrank", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(JudicialroleView(), "Judicialrole", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(LawView(), "Law", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(LawfirmView(), "Lawfirm", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(LawyerView(), "Lawyer", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(LegalreferenceView(), "Legalreference", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(MarkupView(), "Markup", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(MetaDataView(), "MetaData", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ModelView(), "Model", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(NextofkinView(), "Nextofkin", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(NotificationView(), "Notification", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(NotificationregisterView(), "Notificationregister", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(NotificationtypeView(), "Notificationtype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(NotifyeventView(), "Notifyevent", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PageView(), "Page", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PartyView(), "Party", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PartytypeView(), "Partytype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PaymentView(), "Payment", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PersonaleffectView(), "Personaleffect", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PersonaleffectscategoryView(), "Personaleffectscategory", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PoliceofficerView(), "Policeofficer", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PoliceofficerrankView(), "Policeofficerrank", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PolicestationView(), "Policestation", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PolicestationrankView(), "Policestationrank", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PrisonView(), "Prison", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PrisonofficerView(), "Prisonofficer", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(PrisonofficerrankView(), "Prisonofficerrank", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ProsecutorView(), "Prosecutor", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ProsecutorteamView(), "Prosecutorteam", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ReleasetypeView(), "Releasetype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(ReligionView(), "Religion", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(SchedulestatustypeView(), "Schedulestatustype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(SeizureView(), "Seizure", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(SettlementView(), "Settlement", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(SubcountyView(), "Subcounty", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(TemplatetypeView(), "Templatetype", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(TownView(), "Town", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(TranscriptView(), "Transcript", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(VehicleView(), "Vehicle", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(WardView(), "Ward", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(WarranttypeView(), "Warranttype", icon="fa-folder-open-o", category="Setup")




####################
# Join Table Registrations
####################
appbuilder.add_view_no_menu(t_casecategory_courtcaseView(), "t_casecategory_courtcase")

appbuilder.add_view_no_menu(t_casecategorychecklistView(), "t_casecategorychecklist")

appbuilder.add_view_no_menu(t_complaint_complaintcategoryView(), "t_complaint_complaintcategory")

appbuilder.add_view_no_menu(t_complaint_courtcaseView(), "t_complaint_courtcase")

appbuilder.add_view_no_menu(t_court_judicialofficerView(), "t_court_judicialofficer")

appbuilder.add_view_no_menu(t_courtcase_judicialofficerView(), "t_courtcase_judicialofficer")

appbuilder.add_view_no_menu(t_courtcase_lawfirmView(), "t_courtcase_lawfirm")

appbuilder.add_view_no_menu(t_csi_equipment_investigationdiaryView(), "t_csi_equipment_investigationdiary")

appbuilder.add_view_no_menu(t_document_documenttypeView(), "t_document_documenttype")

appbuilder.add_view_no_menu(t_expert_experttypeView(), "t_expert_experttype")

appbuilder.add_view_no_menu(t_hearing_issueView(), "t_hearing_issue")

appbuilder.add_view_no_menu(t_hearing_judicialofficerView(), "t_hearing_judicialofficer")

appbuilder.add_view_no_menu(t_hearing_lawfirmView(), "t_hearing_lawfirm")

appbuilder.add_view_no_menu(t_hearing_lawfirm_2View(), "t_hearing_lawfirm_2")

appbuilder.add_view_no_menu(t_instancecrime_issueView(), "t_instancecrime_issue")

appbuilder.add_view_no_menu(t_investigating_officer_investigationdiaryView(), "t_investigating_officer_investigationdiary")

appbuilder.add_view_no_menu(t_investigationdiary_partyView(), "t_investigationdiary_party")

appbuilder.add_view_no_menu(t_investigationdiary_vehicleView(), "t_investigationdiary_vehicle")

appbuilder.add_view_no_menu(t_issue_lawyerView(), "t_issue_lawyer")

appbuilder.add_view_no_menu(t_issue_legalreferenceView(), "t_issue_legalreference")

appbuilder.add_view_no_menu(t_issue_legalreference_2View(), "t_issue_legalreference_2")

appbuilder.add_view_no_menu(t_issue_partyView(), "t_issue_party")

appbuilder.add_view_no_menu(t_issue_party_2View(), "t_issue_party_2")

appbuilder.add_view_no_menu(t_lawyer_partyView(), "t_lawyer_party")

appbuilder.add_view_no_menu(t_party_settlementView(), "t_party_settlement")

appbuilder.add_view_no_menu(t_policeofficer_policestationView(), "t_policeofficer_policestation")

appbuilder.add_view_no_menu(t_town_wardView(), "t_town_ward")




####################
# Register Join Table MultiViews Registrations
####################
appbuilder.add_view(t_casecategory_courtcaseMultiView(), "['Casecategory', 'Courtcase'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_casecategorychecklistMultiView(), "['Casecategorychecklist'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_complaint_complaintcategoryMultiView(), "['Complaint', 'Complaintcategory'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_complaint_courtcaseMultiView(), "['Complaint', 'Courtcase'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_court_judicialofficerMultiView(), "['Court', 'Judicialofficer'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_courtcase_judicialofficerMultiView(), "['Courtcase', 'Judicialofficer'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_courtcase_lawfirmMultiView(), "['Courtcase', 'Lawfirm'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_csi_equipment_investigationdiaryMultiView(), "['Csi', 'Equipment', 'Investigationdiary'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_document_documenttypeMultiView(), "['Document', 'Documenttype'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_expert_experttypeMultiView(), "['Expert', 'Experttype'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_hearing_issueMultiView(), "['Hearing', 'Issue'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_hearing_judicialofficerMultiView(), "['Hearing', 'Judicialofficer'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_hearing_lawfirmMultiView(), "['Hearing', 'Lawfirm'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_hearing_lawfirm_2MultiView(), "['Hearing', 'Lawfirm', '2'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_instancecrime_issueMultiView(), "['Instancecrime', 'Issue'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_investigating_officer_investigationdiaryMultiView(), "['Investigating', 'Officer', 'Investigationdiary'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_investigationdiary_partyMultiView(), "['Investigationdiary', 'Party'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_investigationdiary_vehicleMultiView(), "['Investigationdiary', 'Vehicle'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_issue_lawyerMultiView(), "['Issue', 'Lawyer'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_issue_legalreferenceMultiView(), "['Issue', 'Legalreference'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_issue_legalreference_2MultiView(), "['Issue', 'Legalreference', '2'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_issue_partyMultiView(), "['Issue', 'Party'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_issue_party_2MultiView(), "['Issue', 'Party', '2'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_lawyer_partyMultiView(), "['Lawyer', 'Party'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_party_settlementMultiView(), "['Party', 'Settlement'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_policeofficer_policestationMultiView(), "['Policeofficer', 'Policestation'] Multi View", icon="fa-address-card-o", category="MultiViews")

appbuilder.add_view(t_town_wardMultiView(), "['Town', 'Ward'] Multi View", icon="fa-address-card-o", category="MultiViews")




####################
# Chart View Registrations
####################
appbuilder.add_view(AccounttypeChartView(), "Accounttype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(AuditMixinChartView(), "AuditMixin Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(BillChartView(), "Bill Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(BilldetailChartView(), "Billdetail Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(BiodatumChartView(), "Biodatum Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CasecategoryChartView(), "Casecategory Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CasechecklistChartView(), "Casechecklist Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CaselinktypeChartView(), "Caselinktype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CelltypeChartView(), "Celltype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CommitalChartView(), "Commital Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CommitaltypeChartView(), "Commitaltype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ComplaintChartView(), "Complaint Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ComplaintcategoryChartView(), "Complaintcategory Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ComplaintroleChartView(), "Complaintrole Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CountryChartView(), "Country Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CountyChartView(), "County Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CourtChartView(), "Court Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CourtaccountChartView(), "Courtaccount Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CourtcaseChartView(), "Courtcase Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CourtrankChartView(), "Courtrank Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CourtstationChartView(), "Courtstation Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CrimeChartView(), "Crime Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(CsiEquipmentChartView(), "CsiEquipment Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(DiagramChartView(), "Diagram Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(DisciplineChartView(), "Discipline Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(DoctemplateChartView(), "Doctemplate Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(DocumentChartView(), "Document Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(DocumenttypeChartView(), "Documenttype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(EconomicclasChartView(), "Economicclas Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ExhibitChartView(), "Exhibit Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ExpertChartView(), "Expert Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ExperttestimonyChartView(), "Experttestimony Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ExperttypeChartView(), "Experttype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(FeeclasChartView(), "Feeclas Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(FeetypeChartView(), "Feetype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(FetchedValueChartView(), "FetchedValue Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(FileColumnChartView(), "FileColumn Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(HealtheventChartView(), "Healthevent Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(HealtheventtypeChartView(), "Healtheventtype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(HearingChartView(), "Hearing Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(HearingtypeChartView(), "Hearingtype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ImageColumnChartView(), "ImageColumn Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ImageManagerChartView(), "ImageManager Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(InstancecrimeChartView(), "Instancecrime Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(InterviewChartView(), "Interview Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(InvestigatingOfficerChartView(), "InvestigatingOfficer Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(InvestigationdiaryChartView(), "Investigationdiary Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(IssueChartView(), "Issue Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(JudicialofficerChartView(), "Judicialofficer Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(JudicialrankChartView(), "Judicialrank Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(JudicialroleChartView(), "Judicialrole Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(LawChartView(), "Law Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(LawfirmChartView(), "Lawfirm Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(LawyerChartView(), "Lawyer Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(LegalreferenceChartView(), "Legalreference Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(MarkupChartView(), "Markup Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(MetaDataChartView(), "MetaData Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ModelChartView(), "Model Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(NextofkinChartView(), "Nextofkin Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(NotificationChartView(), "Notification Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(NotificationregisterChartView(), "Notificationregister Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(NotificationtypeChartView(), "Notificationtype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(NotifyeventChartView(), "Notifyevent Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PageChartView(), "Page Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PartyChartView(), "Party Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PartytypeChartView(), "Partytype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PaymentChartView(), "Payment Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PersonaleffectChartView(), "Personaleffect Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PersonaleffectscategoryChartView(), "Personaleffectscategory Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PoliceofficerChartView(), "Policeofficer Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PoliceofficerrankChartView(), "Policeofficerrank Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PolicestationChartView(), "Policestation Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PolicestationrankChartView(), "Policestationrank Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PrisonChartView(), "Prison Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PrisonofficerChartView(), "Prisonofficer Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(PrisonofficerrankChartView(), "Prisonofficerrank Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ProsecutorChartView(), "Prosecutor Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ProsecutorteamChartView(), "Prosecutorteam Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ReleasetypeChartView(), "Releasetype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(ReligionChartView(), "Religion Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(SchedulestatustypeChartView(), "Schedulestatustype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(SeizureChartView(), "Seizure Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(SettlementChartView(), "Settlement Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(SubcountyChartView(), "Subcounty Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(TemplatetypeChartView(), "Templatetype Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(TownChartView(), "Town Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(TranscriptChartView(), "Transcript Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(VehicleChartView(), "Vehicle Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(WardChartView(), "Ward Age Chart", icon="fa-bar-chart", category="Charts")

appbuilder.add_view(WarranttypeChartView(), "Warranttype Age Chart", icon="fa-bar-chart", category="Charts")




appbuilder.security_cleanup()



####################
# Programming Notes and things of interest
####################

# appbuilder.add_separator("Setup")
# appbuilder.add_separator("My Views")
# appbuilder.add_link(name, href, icon='', label='', category='', category_icon='', category_label='', baseview=None)




####################
# Join Table List
####################

# t_casecategory_courtcase -['Casecategory', 'Courtcase']

# t_casecategorychecklist -['Casecategorychecklist']

# t_complaint_complaintcategory -['Complaint', 'Complaintcategory']

# t_complaint_courtcase -['Complaint', 'Courtcase']

# t_court_judicialofficer -['Court', 'Judicialofficer']

# t_courtcase_judicialofficer -['Courtcase', 'Judicialofficer']

# t_courtcase_lawfirm -['Courtcase', 'Lawfirm']

# t_csi_equipment_investigationdiary -['Csi', 'Equipment', 'Investigationdiary']

# t_document_documenttype -['Document', 'Documenttype']

# t_expert_experttype -['Expert', 'Experttype']

# t_hearing_issue -['Hearing', 'Issue']

# t_hearing_judicialofficer -['Hearing', 'Judicialofficer']

# t_hearing_lawfirm -['Hearing', 'Lawfirm']

# t_hearing_lawfirm_2 -['Hearing', 'Lawfirm', '2']

# t_instancecrime_issue -['Instancecrime', 'Issue']

# t_investigating_officer_investigationdiary -['Investigating', 'Officer', 'Investigationdiary']

# t_investigationdiary_party -['Investigationdiary', 'Party']

# t_investigationdiary_vehicle -['Investigationdiary', 'Vehicle']

# t_issue_lawyer -['Issue', 'Lawyer']

# t_issue_legalreference -['Issue', 'Legalreference']

# t_issue_legalreference_2 -['Issue', 'Legalreference', '2']

# t_issue_party -['Issue', 'Party']

# t_issue_party_2 -['Issue', 'Party', '2']

# t_lawyer_party -['Lawyer', 'Party']

# t_party_settlement -['Party', 'Settlement']

# t_policeofficer_policestation -['Policeofficer', 'Policestation']

# t_town_ward -['Town', 'Ward']



####################
# List of tables
####################

# Accounttype

# AuditMixin

# Bill

# Billdetail

# Biodatum

# Casecategory

# Casechecklist

# Caselinktype

# Celltype

# Commital

# Commitaltype

# Complaint

# Complaintcategory

# Complaintrole

# Country

# County

# Court

# Courtaccount

# Courtcase

# Courtrank

# Courtstation

# Crime

# CsiEquipment

# Diagram

# Discipline

# Doctemplate

# Document

# Documenttype

# Economicclas

# Exhibit

# Expert

# Experttestimony

# Experttype

# Feeclas

# Feetype

# FetchedValue

# FileColumn

# Healthevent

# Healtheventtype

# Hearing

# Hearingtype

# ImageColumn

# ImageManager

# Instancecrime

# Interview

# InvestigatingOfficer

# Investigationdiary

# Issue

# Judicialofficer

# Judicialrank

# Judicialrole

# Law

# Lawfirm

# Lawyer

# Legalreference

# Markup

# MetaData

# Model

# Nextofkin

# Notification

# Notificationregister

# Notificationtype

# Notifyevent

# Page

# Party

# Partytype

# Payment

# Personaleffect

# Personaleffectscategory

# Policeofficer

# Policeofficerrank

# Policestation

# Policestationrank

# Prison

# Prisonofficer

# Prisonofficerrank

# Prosecutor

# Prosecutorteam

# Releasetype

# Religion

# Schedulestatustype

# Seizure

# Settlement

# Subcounty

# Templatetype

# Town

# Transcript

# Vehicle

# Ward

# Warranttype
