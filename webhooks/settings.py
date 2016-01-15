conf = {
    # 'api_token': '4b61f2fb79d095ad428c1850ae091f1e993a4b4e',
    'api_token': 'c8cde9dbbdda6f544018e9321d017e909b28ec51',
    'default_api_uri': 'http://localhost:8000/api/v1/contacts.json',
    'queuing_db_connection_string': "dbname=skytools user=postgres",
}

MAPPING = {
    'apt_emtct_expected': {
        'descr': 'Expected eMTCT Mothers on Appointment',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'xVpHSWaIBEX'
    },
    'apt_emtct_missed': {
        'descr': 'eMTCT Missed Appointments',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'LYT11E96lC5'
    },
    'apt_opd_new': {
        'descr': 'OPD New Attendees',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'xqSBj2KUlas'
    },
    'apt_opd_total': {
        'descr': 'OPT Total Attendence',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'xb4g6Zf7fAT'
    },
    'arv_emtct': {
        'descr': 'ARVs (Fixed - DC eMTCT)',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'xgSJLvdm2cQ'
    },
    'arv_nevirapine': {
        'descr': 'Nevirapine Therapy',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'JPVp2yLEimL'
    },
    'arv_hiv_screening_test_kits': {
        'descr': 'HIV screening test kits',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'kteQimFQJom'
    },
    'cases_ab': {
        'descr': 'Cases of Animal Bites',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'mdIPCPfqXaJ'},
    'cases_ae': {
        'descr': 'Cases of Adverse Events Following Immunization',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'fTwT8uX9Uto'
    },
    'cases_af': {
        'descr': 'Cases of Acute Flacid Paralysis',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'U7cokRIptxu'
    },
    'cases_ch': {
        'descr': 'Cases of Cholera',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'FPsN2bDpRru'
    },
    'cases_dy': {
        'descr': 'Cases of Dysentery',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'NoJfAIcxjSY'
    },
    'cases_gw': {
        'descr': 'Cases of Guinea Worm',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'hzGgkiOjfRs'
    },
    'cases_id': {
        'descr': 'Cases of Other Emerging Infectious Diseases',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'ZZrhG7CYNjy'
    },
    'cases_ma': {
        'descr': 'Cases of Malaria',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'fclvwNhzu7d'
    },
    'cases_me': {
        'descr': 'Cases of Measles',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'v8HuPNb03yq'
    },
    'cases_mg': {
        'descr': 'Cases of Bacterial Meningitis',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'JxUexqKeXtZ'},
    'cases_nt': {
        'descr': 'Cases of Neonatal Tetanus',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'euf2TqlswFp'
    },
    'cases_pl': {
        'descr': 'Cases of Plague',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'peyFcHisgZB'
    },
    'cases_rb': {
        'descr': 'Cases of Rabies',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'tTGAElxDIWg'
    },
    'cases_sa': {
        'descr': 'Cases of Severe Acute Respiratory Infection',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'MHtpmIQEnyc'
    },
    'cases_tb': {
        'descr': 'Presumptive Multi Drug Resistance (MDR) TB',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'yzdPKhvgeXq'},
    'cases_tf': {
        'descr': 'Cases of Typhoid Fever',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'IkI01xB7RIi'
    },
    'cases_vf': {
        'descr': 'Cases of Other Viral Hemorrhagic Fevers',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'BMJMdxh1Loy'
    },
    'cases_yf': {
        'descr': 'Cases of Yellow Fever',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'OE8baEzA2Cq'
    },
    'death_ab': {
        'descr': 'Deaths from Animal Bites',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'UKYPpKnSBK4'
    },
    'death_ae': {
        'descr': 'Deaths from Adverse Events Following Immunization',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'k2dUb4N7D0D'
    },
    'death_af': {
        'descr': 'Deaths from Acute Flacid Paralysis',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'XzYd9m4XaKS'
    },
    'death_ch': {
        'descr': 'Deaths from Cholera',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'QP9yftzrkne'
    },
    'death_dy': {
        'descr': 'Deaths from Dysentery',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'JTc25LIvtQb'
    },
    'death_gw': {
        'descr': 'Deaths from Guinea Worm',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'yvbPC5zDb3c'
    },
    'death_id': {
        'descr': 'Deaths from Other Emerging Infectious Diseases',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'qHSErXOlcf3'
    },
    'death_ma': {
        'descr': 'Deaths from Malaria',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'YXIu5CW9LPR'
    },
    'death_md': {
        'descr': 'Maternal deaths',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'ck3jFjr8fOT'
    },
    'death_me': {
        'descr': 'Deaths from Measles',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'tjTnFJ1QdVz'
    },
    'death_mg': {
        'descr': 'Deaths from Bacterial Meningitis',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'r3xIBQaeLsT'},
    'death_nt': {
        'descr': 'Deaths from Neonatal Tetanus',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'tIh9TQxGOJU'
    },
    'death_pd': {
        'descr': 'Perinatal deaths',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'nG5hrCX3vyP'
    },
    'death_pl': {
        'descr': 'Deaths from Plague',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'hBcX7S7xBcu'
    },
    'death_rb': {
        'descr': 'Deaths from Rabies',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'Dy90lwS6c6x'
    },
    'death_sa': {
        'descr': 'Deaths from Severe Acute Respiratory Infection',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'qdZbdsCpIr7'
    },
    'death_tb': {
        'descr': 'Presumptive Multi Drug Resistance (MDR) TB',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'eEruojUV6Jh'
    },
    'death_tf': {
        'descr': 'Deaths from Typhoid Fever',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'OMxmmYvvLai'
    },
    'death_vf': {
        'descr': 'Deaths from Other Viral Hemorrhagic Fevers',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'BX2PYPKm8F9'
    },
    'death_yf': {
        'descr': 'Deaths from Yellow Fever',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'w3mO7SZdbb8'
    },
    'mat_microscopy_neg_treated': {
        'descr': 'Microscopy negative cases treated',
        'dhis2_combo_id': 'TTwU8Bv4fKm',
        'dhis2_uuid': 'ZgPtploqq0L'
    },
    'mat_microscopy_positive': {
        'descr': 'Microscopy positive cases',
        'dhis2_combo_id': '3rYpFjLrrYa',
        'dhis2_uuid': 'KPmTI3TGwZw'
    },
    'mat_microscopy_pos_treated': {
        'descr': 'Microscopy positive cases treated',
        'dhis2_combo_id': 'vp37EZVg3xG',
        'dhis2_uuid': 'ZgPtploqq0L'
    },
    'mat_microscopy_tested': {
        'descr': 'Microscopy tested cases',
        'dhis2_combo_id': 't8Jv78lnSbU',
        'dhis2_uuid': 'KPmTI3TGwZw'
    },
    'mat_not_tested_treated': {
        'descr': 'Not tested cases treated',
        'dhis2_combo_id': 'w16OBdsg4b7',
        'dhis2_uuid': 'ZgPtploqq0L'
    },
    'mat_rdt_neg_treated': {
        'descr': 'RDT negative cases treated',
        'dhis2_combo_id': 'NfJyyb1eBaw',
        'dhis2_uuid': 'ZgPtploqq0L'
    },
    'mat_rdt_positive': {
        'descr': 'RDT positive cases',
        'dhis2_combo_id': 'PfdPCxOoiBj',
        'dhis2_uuid': 'KPmTI3TGwZw'
    },
    'mat_rdt_pos_treated': {
        'descr': 'RDT positive cases treated',
        'dhis2_combo_id': 'QOWAmZ7jBno',
        'dhis2_uuid': 'ZgPtploqq0L'
    },
    'mat_rdt_tesed': {
        'descr': 'RDT tested cases',
        'dhis2_combo_id': 'kcXY5cWAOsB',
        'dhis2_uuid': 'KPmTI3TGwZw'
    },
    'mat_suspected_malaria': {
        'descr': 'Suspected Malaria (fever)',
        'dhis2_combo_id': '3W3d2AqT4Aq',
        'dhis2_uuid': 'KPmTI3TGwZw'
    },
    'tra_act_tablets': {
        'descr': 'ACT (Tablets)',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'Ju0Cann41Ul'
    },
    'tra_amoxcilline': {
        'descr': 'Amoxcilline',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'tFrWdigZ4oo'
    },
    'tra_depo_provera': {
        'descr': 'Depo - Provera',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'v6ACxYNPIvm'
    },
    'tra_fansidar': {
        'descr': 'Fansidar',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'fX6A6NO18pY'
    },
    'tra_iv_artesunate': {
        'descr': 'IV artesunate',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'O2OrXuZo4hB'
    },
    'tra_measles_vaccine': {
        'descr': 'Measles Vaccine',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'DgeykDdSLzI'
    },
    'tra_ors': {
        'descr': 'ORS (Scakets)',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'zmimiDOJwaf'
    },
    'tra_rdt_malaria': {
        'descr': 'Malaria RDTs',
        'dhis2_combo_id': 'gGhClrV5odI',
        'dhis2_uuid': 'CzsKMvQDwMV'
    }
}

XML_TEMPLATE = """
<dataValueSet xmlns="http://dhis2.org/schema/dxf/2.0" dataSet="V1kJRs8CtW4" completeDate="%(complete_date)s" period="%(period)s" orgUnitIdScheme="uuid" orgUnit="%(orgunit)s">
<dataValues>
    %(datavales)s
</dataValues>
</dataValueSet>
"""

DEFAULT_DATA_VALUES = {
    'cases': "<dataValue dataElement='fclvwNhzu7d' categoryOptionCombo='gGhClrV5odI' value='0' />",
    'death': "<dataValue dataElement='YXIu5CW9LPR' categoryOptionCombo='gGhClrV5odI' value='0' />"
}
