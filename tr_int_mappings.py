from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TrnsInt(Base):
    __tablename__ = "trns_it"
    __table_args__ = {'schema': 'infohub'}

    trns_it_id = Column(Integer, primary_key=True)
    source_file_id = Column(Integer)
    dataset_list_id = Column(Integer)
    mng_ppl_id = Column(Integer)
    pipeline_code = Column(String)
    pipeline_name = Column(String)
    pipeline_prop_name = Column(String)
    report_dt = Column(DateTime)
    report_amend_desc = Column(String)
    footnote_item_list = Column(String)
    crt_dt = Column(DateTime, default=func.now())
    crt_usr = Column(String, default='system')

    trns_it_k = relationship("TrnsIntK", back_populates="trns_it")

    def __init__(self):
        self.trns_it_k = []


class TrnsIntK(Base):
    __tablename__ = "trns_it_k"
    __table_args__ = {'schema': 'infohub'}

    trns_it_k_id = Column(Integer, primary_key=True)
    rate_schedule = Column(String)
    k_holder = Column(String)
    k_holder_name = Column(String)
    k_holder_prop = Column(String)
    svc_req_k = Column(String)
    k_roll = Column(String)
    k_roll_desc = Column(String)
    k_status = Column(String)
    k_status_desc = Column(String)
    k_beg_date = Column(DateTime)
    k_end_date = Column(DateTime)
    affil = Column(String)
    affil_ind_desc = Column(String)
    surchg_ind = Column(String)
    surchg_ind_desc = Column(String)
    term_notes = Column(String)
    res_rate_basis_desc = Column(String)
    crt_dt = Column(DateTime, default=func.now())
    crt_usr = Column(String, default='system')

    trns_it_k_ind = relationship("TrnsIntKInd", back_populates="trns_it_k")
    trns_it_limit = relationship("TrnsIntLimit", back_populates="trns_it_k")
    trns_it_rate = relationship("TrnsIntRate", back_populates="trns_it_k")

    trns_it_id = Column(Integer, ForeignKey('infohub.trns_it.trns_it_id'))
    trns_it = relationship("TrnsInt", back_populates="trns_it_k")

    def __init__(self):
        self.trns_it_k_ind = []
        self.trns_it_limit = []
        self.trns_it_rate = []


class TrnsIntKInd(Base):
    __tablename__ = "trns_it_k_ind"
    __table_args__ = {'schema': 'infohub'}

    trns_it_k_ind_id = Column(Integer, primary_key=True)
    neg_rates_ind = Column(String)
    neg_rates_ind_desc = Column(String)
    market_based_rate_ind = Column(String)
    discount_ind = Column(String)
    discount_ind_desc = Column(String)
    surchg_ind = Column(String)
    surchg_ind_desc = Column(String)
    beg_date = Column(DateTime)
    end_date = Column(DateTime)
    crt_dt = Column(DateTime, default=func.now())
    crt_usr = Column(String, default='system')

    trns_it_k_id = Column(Integer, ForeignKey('infohub.trns_it_k.trns_it_k_id'))
    trns_it_k = relationship("TrnsIntK", back_populates="trns_it_k_ind")


class TrnsIntLimit(Base):
    __tablename__ = "trns_it_limit"
    __table_args__ = {'schema': 'infohub'}

    trns_it_limit_id = Column(Integer, primary_key=True)
    loc_based_limit_ind = Column(Integer)
    loc = Column(String)
    loc_name = Column(String)
    loc_purp = Column(String)
    loc_purp_desc = Column(String)
    loc_qti = Column(String)
    loc_qti_desc = Column(String)
    loc_zn = Column(String)
    k_qty_loc = Column(Integer)
    limit_type = Column(String)
    beg_date = Column(DateTime)
    end_date = Column(DateTime)
    qty_units = Column(String)
    crt_dt = Column(DateTime, default=func.now())
    crt_usr = Column(String, default='system')

    trns_it_k_id = Column(Integer, ForeignKey('infohub.trns_it_k.trns_it_k_id'))
    trns_it_k = relationship("TrnsIntK", back_populates="trns_it_limit")


class TrnsIntRate(Base):
    __tablename__ = "trns_it_rate"
    __table_args__ = {'schema': 'infohub'}

    trns_it_rate_id = Column(Integer, primary_key=True)
    shrinkage_ind = Column(Integer)
    surchg_id = Column(String)
    surchg_id_desc = Column(String)
    chrg_id = Column(String)
    rate_id = Column(String)
    rate_id_desc = Column(String)
    tier_type = Column(String)
    beg_date = Column(DateTime)
    end_date = Column(DateTime)
    rec_loc = Column(String)
    rec_loc_name = Column(String)
    del_loc = Column(String)
    del_loc_name = Column(String)
    tier_low = Column(String)
    tier_high = Column(String)
    index_nm = Column(String)
    formula = Column(String)
    adj_factor = Column(String)
    rate_chrg_ref = Column(String)
    rate_chrg_ref_desc = Column(String)
    rpt_lvl = Column(String)
    rpt_lvl_desc = Column(String)
    total_surchg = Column(Integer)
    rate_chrg = Column(String)
    qty_units = Column(String)
    max_ref_rate = Column(String)
    max_trf_rate_ref = Column(String)
    max_trf_rate_ref_desc = Column(String)
    crt_dt = Column(DateTime, default=func.now())
    crt_usr = Column(String, default='system')

    trns_it_k_id = Column(Integer, ForeignKey('infohub.trns_it_k.trns_it_k_id'))
    trns_it_k = relationship("TrnsIntK", back_populates="trns_it_rate")
