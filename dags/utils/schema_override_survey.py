from sqlalchemy import NVARCHAR, String
import polars as pl


list_columns_complete_2025 = [
                'answer_id',
                'ResponseId',
                'survey_year',
                'MainBranch',
                'Age',
                'EdLevel',
                'Employment',
                'WorkExp',
                'LearnCode',
                'DevType',
                'OrgSize',
                'ICorPM',
                'RemoteWork',
                'Country',
                'Currency',
                'CompTotal',
                'ConvertedCompYearly',
                'LanguageHaveWorkedWith',
                'LanguageWantToWorkWith',
                'DatabaseHaveWorkedWith',
                'DatabaseWantToWorkWith',
                'PlatformHaveWorkedWith',
                'PlatformWantToWorkWith',
                'WebframeHaveWorkedWith',
                'WebframeWantToWorkWith',
                'SOTagsHaveWorkedWith',
                'SOTagsWantToWorkWith',]

schema_complete_2025 = {}


def get_schema_survey_2025():
    for col in list_columns_complete_2025:
        schema_complete_2025.update({col: pl.String})
    return schema_complete_2025


def get_schema_nolist_2025(schema_complete_2025):
    list_col_remove_2025 = [
                'LanguageHaveWorkedWith',
                'LanguageWantToWorkWith',
                'DatabaseHaveWorkedWith',
                'DatabaseWantToWorkWith',
                'PlatformHaveWorkedWith',
                'PlatformWantToWorkWith',
                'WebframeHaveWorkedWith',
                'WebframeWantToWorkWith',
                'SOTagsHaveWorkedWith',
                'SOTagsWantToWorkWith',]

    schema_no_list_2025 = schema_complete_2025.copy()
    for col in list_col_remove_2025:
        schema_no_list_2025.pop(col)

    return schema_no_list_2025


list_columns_complete_22_24 = [
                'answer_id',
                'ResponseId',
                'survey_year',
                'MainBranch',
                'Age',
                'EdLevel',
                'Employment',
                'WorkExp',
                'LearnCode',
                'DevType',
                'OrgSize',
                'ICorPM',
                'RemoteWork',
                'Country',
                'Currency',
                'CompTotal',
                'ConvertedCompYearly',
                'LanguageHaveWorkedWith',
                'LanguageWantToWorkWith',
                'DatabaseHaveWorkedWith',
                'DatabaseWantToWorkWith',
                'PlatformHaveWorkedWith',
                'PlatformWantToWorkWith',
                'WebframeHaveWorkedWith',
                'WebframeWantToWorkWith',
                'MiscTechHaveWorkedWith',
                'MiscTechWantToWorkWith',
                'ToolsTechHaveWorkedWith',
                'ToolsTechWantToWorkWith',              
                ]

schema_complete_22_24 = {}


def get_schema_survey_22_24():
    for col in list_columns_complete_22_24:
        schema_complete_22_24.update({col: pl.String})
    return schema_complete_22_24


def get_schema_nolist_22_24(schema_complete_22_24):
    list_col_remove_22_24 = [
                'LanguageHaveWorkedWith',
                'LanguageWantToWorkWith',
                'DatabaseHaveWorkedWith',
                'DatabaseWantToWorkWith',
                'PlatformHaveWorkedWith',
                'PlatformWantToWorkWith',
                'WebframeHaveWorkedWith',
                'WebframeWantToWorkWith',
                'MiscTechHaveWorkedWith',
                'MiscTechWantToWorkWith',
                'ToolsTechHaveWorkedWith',
                'ToolsTechWantToWorkWith',]

    schema_no_list_22_24 = schema_complete_22_24.copy()
    for col in list_col_remove_22_24:
        schema_no_list_22_24.pop(col)

    return schema_no_list_22_24
