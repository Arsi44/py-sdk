# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/distribution/v1beta1/distribution.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n.cosmos/distribution/v1beta1/distribution.proto\x12\x1b\x63osmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x8a\x03\n\x06Params\x12]\n\rcommunity_tax\x18\x01 \x01(\tBF\xf2\xde\x1f\x14yaml:\"community_tax\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12k\n\x14\x62\x61se_proposer_reward\x18\x02 \x01(\tBM\xf2\xde\x1f\x1byaml:\"base_proposer_reward\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12m\n\x15\x62onus_proposer_reward\x18\x03 \x01(\tBN\xf2\xde\x1f\x1cyaml:\"bonus_proposer_reward\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12?\n\x15withdraw_addr_enabled\x18\x04 \x01(\x08\x42 \xf2\xde\x1f\x1cyaml:\"withdraw_addr_enabled\":\x04\x98\xa0\x1f\x00\"\xe8\x01\n\x1aValidatorHistoricalRewards\x12\x94\x01\n\x17\x63umulative_reward_ratio\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinBU\xf2\xde\x1f\x1eyaml:\"cumulative_reward_ratio\"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12\x33\n\x0freference_count\x18\x02 \x01(\rB\x1a\xf2\xde\x1f\x16yaml:\"reference_count\"\"\x8d\x01\n\x17ValidatorCurrentRewards\x12\x62\n\x07rewards\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12\x0e\n\x06period\x18\x02 \x01(\x04\"\x87\x01\n\x1eValidatorAccumulatedCommission\x12\x65\n\ncommission\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\"\x93\x01\n\x1bValidatorOutstandingRewards\x12t\n\x07rewards\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinBE\xf2\xde\x1f\x0eyaml:\"rewards\"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\"\x8e\x01\n\x13ValidatorSlashEvent\x12\x35\n\x10validator_period\x18\x01 \x01(\x04\x42\x1b\xf2\xde\x1f\x17yaml:\"validator_period\"\x12@\n\x08\x66raction\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\x95\x01\n\x14ValidatorSlashEvents\x12w\n\x16validator_slash_events\x18\x01 \x03(\x0b\x32\x30.cosmos.distribution.v1beta1.ValidatorSlashEventB%\xf2\xde\x1f\x1dyaml:\"validator_slash_events\"\xc8\xde\x1f\x00:\x04\x98\xa0\x1f\x00\"\x8e\x01\n\x07\x46\x65\x65Pool\x12\x82\x01\n\x0e\x63ommunity_pool\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinBL\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xf2\xde\x1f\x15yaml:\"community_pool\"\"\xbe\x01\n\x1a\x43ommunityPoolSpendProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12[\n\x06\x61mount\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\xda\x01\n\x15\x44\x65legatorStartingInfo\x12\x33\n\x0fprevious_period\x18\x01 \x01(\x04\x42\x1a\xf2\xde\x1f\x16yaml:\"previous_period\"\x12M\n\x05stake\x18\x02 \x01(\tB>\xf2\xde\x1f\x0cyaml:\"stake\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12=\n\x06height\x18\x03 \x01(\x04\x42-\xf2\xde\x1f\x16yaml:\"creation_height\"\xea\xde\x1f\x0f\x63reation_height\"\xc1\x01\n\x19\x44\x65legationDelegatorReward\x12\x37\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\"\x12\x61\n\x06reward\x18\x02 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01\"\xf0\x01\n%CommunityPoolSpendProposalWithDeposit\x12\x1f\n\x05title\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"title\"\x12+\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"description\"\x12\'\n\trecipient\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"recipient\"\x12!\n\x06\x61mount\x18\x04 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"amount\"\x12#\n\x07\x64\x65posit\x18\x05 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"deposit\":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01\x42\x37Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01\x62\x06proto3'
)


_PARAMS = DESCRIPTOR.message_types_by_name['Params']
_VALIDATORHISTORICALREWARDS = DESCRIPTOR.message_types_by_name['ValidatorHistoricalRewards']
_VALIDATORCURRENTREWARDS = DESCRIPTOR.message_types_by_name['ValidatorCurrentRewards']
_VALIDATORACCUMULATEDCOMMISSION = DESCRIPTOR.message_types_by_name['ValidatorAccumulatedCommission']
_VALIDATOROUTSTANDINGREWARDS = DESCRIPTOR.message_types_by_name['ValidatorOutstandingRewards']
_VALIDATORSLASHEVENT = DESCRIPTOR.message_types_by_name['ValidatorSlashEvent']
_VALIDATORSLASHEVENTS = DESCRIPTOR.message_types_by_name['ValidatorSlashEvents']
_FEEPOOL = DESCRIPTOR.message_types_by_name['FeePool']
_COMMUNITYPOOLSPENDPROPOSAL = DESCRIPTOR.message_types_by_name['CommunityPoolSpendProposal']
_DELEGATORSTARTINGINFO = DESCRIPTOR.message_types_by_name['DelegatorStartingInfo']
_DELEGATIONDELEGATORREWARD = DESCRIPTOR.message_types_by_name['DelegationDelegatorReward']
_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT = DESCRIPTOR.message_types_by_name['CommunityPoolSpendProposalWithDeposit']
Params = _reflection.GeneratedProtocolMessageType(
    'Params',
    (_message.Message,),
    {
        'DESCRIPTOR': _PARAMS,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.Params)
    },
)
_sym_db.RegisterMessage(Params)

ValidatorHistoricalRewards = _reflection.GeneratedProtocolMessageType(
    'ValidatorHistoricalRewards',
    (_message.Message,),
    {
        'DESCRIPTOR': _VALIDATORHISTORICALREWARDS,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorHistoricalRewards)
    },
)
_sym_db.RegisterMessage(ValidatorHistoricalRewards)

ValidatorCurrentRewards = _reflection.GeneratedProtocolMessageType(
    'ValidatorCurrentRewards',
    (_message.Message,),
    {
        'DESCRIPTOR': _VALIDATORCURRENTREWARDS,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorCurrentRewards)
    },
)
_sym_db.RegisterMessage(ValidatorCurrentRewards)

ValidatorAccumulatedCommission = _reflection.GeneratedProtocolMessageType(
    'ValidatorAccumulatedCommission',
    (_message.Message,),
    {
        'DESCRIPTOR': _VALIDATORACCUMULATEDCOMMISSION,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorAccumulatedCommission)
    },
)
_sym_db.RegisterMessage(ValidatorAccumulatedCommission)

ValidatorOutstandingRewards = _reflection.GeneratedProtocolMessageType(
    'ValidatorOutstandingRewards',
    (_message.Message,),
    {
        'DESCRIPTOR': _VALIDATOROUTSTANDINGREWARDS,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorOutstandingRewards)
    },
)
_sym_db.RegisterMessage(ValidatorOutstandingRewards)

ValidatorSlashEvent = _reflection.GeneratedProtocolMessageType(
    'ValidatorSlashEvent',
    (_message.Message,),
    {
        'DESCRIPTOR': _VALIDATORSLASHEVENT,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorSlashEvent)
    },
)
_sym_db.RegisterMessage(ValidatorSlashEvent)

ValidatorSlashEvents = _reflection.GeneratedProtocolMessageType(
    'ValidatorSlashEvents',
    (_message.Message,),
    {
        'DESCRIPTOR': _VALIDATORSLASHEVENTS,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorSlashEvents)
    },
)
_sym_db.RegisterMessage(ValidatorSlashEvents)

FeePool = _reflection.GeneratedProtocolMessageType(
    'FeePool',
    (_message.Message,),
    {
        'DESCRIPTOR': _FEEPOOL,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.FeePool)
    },
)
_sym_db.RegisterMessage(FeePool)

CommunityPoolSpendProposal = _reflection.GeneratedProtocolMessageType(
    'CommunityPoolSpendProposal',
    (_message.Message,),
    {
        'DESCRIPTOR': _COMMUNITYPOOLSPENDPROPOSAL,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.CommunityPoolSpendProposal)
    },
)
_sym_db.RegisterMessage(CommunityPoolSpendProposal)

DelegatorStartingInfo = _reflection.GeneratedProtocolMessageType(
    'DelegatorStartingInfo',
    (_message.Message,),
    {
        'DESCRIPTOR': _DELEGATORSTARTINGINFO,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.DelegatorStartingInfo)
    },
)
_sym_db.RegisterMessage(DelegatorStartingInfo)

DelegationDelegatorReward = _reflection.GeneratedProtocolMessageType(
    'DelegationDelegatorReward',
    (_message.Message,),
    {
        'DESCRIPTOR': _DELEGATIONDELEGATORREWARD,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.DelegationDelegatorReward)
    },
)
_sym_db.RegisterMessage(DelegationDelegatorReward)

CommunityPoolSpendProposalWithDeposit = _reflection.GeneratedProtocolMessageType(
    'CommunityPoolSpendProposalWithDeposit',
    (_message.Message,),
    {
        'DESCRIPTOR': _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT,
        '__module__': 'cosmos.distribution.v1beta1.distribution_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit)
    },
)
_sym_db.RegisterMessage(CommunityPoolSpendProposalWithDeposit)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\250\342\036\001'
    _PARAMS.fields_by_name['community_tax']._options = None
    _PARAMS.fields_by_name[
        'community_tax'
    ]._serialized_options = (
        b'\362\336\037\024yaml:\"community_tax\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    )
    _PARAMS.fields_by_name['base_proposer_reward']._options = None
    _PARAMS.fields_by_name[
        'base_proposer_reward'
    ]._serialized_options = b'\362\336\037\033yaml:\"base_proposer_reward\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _PARAMS.fields_by_name['bonus_proposer_reward']._options = None
    _PARAMS.fields_by_name[
        'bonus_proposer_reward'
    ]._serialized_options = b'\362\336\037\034yaml:\"bonus_proposer_reward\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _PARAMS.fields_by_name['withdraw_addr_enabled']._options = None
    _PARAMS.fields_by_name[
        'withdraw_addr_enabled'
    ]._serialized_options = b'\362\336\037\034yaml:\"withdraw_addr_enabled\"'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\230\240\037\000'
    _VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio']._options = None
    _VALIDATORHISTORICALREWARDS.fields_by_name[
        'cumulative_reward_ratio'
    ]._serialized_options = b'\362\336\037\036yaml:\"cumulative_reward_ratio\"\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000'
    _VALIDATORHISTORICALREWARDS.fields_by_name['reference_count']._options = None
    _VALIDATORHISTORICALREWARDS.fields_by_name[
        'reference_count'
    ]._serialized_options = b'\362\336\037\026yaml:\"reference_count\"'
    _VALIDATORCURRENTREWARDS.fields_by_name['rewards']._options = None
    _VALIDATORCURRENTREWARDS.fields_by_name[
        'rewards'
    ]._serialized_options = b'\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000'
    _VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission']._options = None
    _VALIDATORACCUMULATEDCOMMISSION.fields_by_name[
        'commission'
    ]._serialized_options = b'\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000'
    _VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards']._options = None
    _VALIDATOROUTSTANDINGREWARDS.fields_by_name[
        'rewards'
    ]._serialized_options = (
        b'\362\336\037\016yaml:\"rewards\"\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000'
    )
    _VALIDATORSLASHEVENT.fields_by_name['validator_period']._options = None
    _VALIDATORSLASHEVENT.fields_by_name[
        'validator_period'
    ]._serialized_options = b'\362\336\037\027yaml:\"validator_period\"'
    _VALIDATORSLASHEVENT.fields_by_name['fraction']._options = None
    _VALIDATORSLASHEVENT.fields_by_name[
        'fraction'
    ]._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events']._options = None
    _VALIDATORSLASHEVENTS.fields_by_name[
        'validator_slash_events'
    ]._serialized_options = b'\362\336\037\035yaml:\"validator_slash_events\"\310\336\037\000'
    _VALIDATORSLASHEVENTS._options = None
    _VALIDATORSLASHEVENTS._serialized_options = b'\230\240\037\000'
    _FEEPOOL.fields_by_name['community_pool']._options = None
    _FEEPOOL.fields_by_name[
        'community_pool'
    ]._serialized_options = b'\310\336\037\000\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\362\336\037\025yaml:\"community_pool\"'
    _COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount']._options = None
    _COMMUNITYPOOLSPENDPROPOSAL.fields_by_name[
        'amount'
    ]._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
    _COMMUNITYPOOLSPENDPROPOSAL._options = None
    _COMMUNITYPOOLSPENDPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000\230\240\037\000'
    _DELEGATORSTARTINGINFO.fields_by_name['previous_period']._options = None
    _DELEGATORSTARTINGINFO.fields_by_name[
        'previous_period'
    ]._serialized_options = b'\362\336\037\026yaml:\"previous_period\"'
    _DELEGATORSTARTINGINFO.fields_by_name['stake']._options = None
    _DELEGATORSTARTINGINFO.fields_by_name[
        'stake'
    ]._serialized_options = (
        b'\362\336\037\014yaml:\"stake\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    )
    _DELEGATORSTARTINGINFO.fields_by_name['height']._options = None
    _DELEGATORSTARTINGINFO.fields_by_name[
        'height'
    ]._serialized_options = b'\362\336\037\026yaml:\"creation_height\"\352\336\037\017creation_height'
    _DELEGATIONDELEGATORREWARD.fields_by_name['validator_address']._options = None
    _DELEGATIONDELEGATORREWARD.fields_by_name[
        'validator_address'
    ]._serialized_options = b'\362\336\037\030yaml:\"validator_address\"'
    _DELEGATIONDELEGATORREWARD.fields_by_name['reward']._options = None
    _DELEGATIONDELEGATORREWARD.fields_by_name[
        'reward'
    ]._serialized_options = b'\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000'
    _DELEGATIONDELEGATORREWARD._options = None
    _DELEGATIONDELEGATORREWARD._serialized_options = b'\210\240\037\000\230\240\037\001'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['title']._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name[
        'title'
    ]._serialized_options = b'\362\336\037\014yaml:\"title\"'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['description']._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name[
        'description'
    ]._serialized_options = b'\362\336\037\022yaml:\"description\"'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['recipient']._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name[
        'recipient'
    ]._serialized_options = b'\362\336\037\020yaml:\"recipient\"'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['amount']._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name[
        'amount'
    ]._serialized_options = b'\362\336\037\ryaml:\"amount\"'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['deposit']._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name[
        'deposit'
    ]._serialized_options = b'\362\336\037\016yaml:\"deposit\"'
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._options = None
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._serialized_options = b'\210\240\037\000\230\240\037\001'
    _PARAMS._serialized_start = 134
    _PARAMS._serialized_end = 528
    _VALIDATORHISTORICALREWARDS._serialized_start = 531
    _VALIDATORHISTORICALREWARDS._serialized_end = 763
    _VALIDATORCURRENTREWARDS._serialized_start = 766
    _VALIDATORCURRENTREWARDS._serialized_end = 907
    _VALIDATORACCUMULATEDCOMMISSION._serialized_start = 910
    _VALIDATORACCUMULATEDCOMMISSION._serialized_end = 1045
    _VALIDATOROUTSTANDINGREWARDS._serialized_start = 1048
    _VALIDATOROUTSTANDINGREWARDS._serialized_end = 1195
    _VALIDATORSLASHEVENT._serialized_start = 1198
    _VALIDATORSLASHEVENT._serialized_end = 1340
    _VALIDATORSLASHEVENTS._serialized_start = 1343
    _VALIDATORSLASHEVENTS._serialized_end = 1492
    _FEEPOOL._serialized_start = 1495
    _FEEPOOL._serialized_end = 1637
    _COMMUNITYPOOLSPENDPROPOSAL._serialized_start = 1640
    _COMMUNITYPOOLSPENDPROPOSAL._serialized_end = 1830
    _DELEGATORSTARTINGINFO._serialized_start = 1833
    _DELEGATORSTARTINGINFO._serialized_end = 2051
    _DELEGATIONDELEGATORREWARD._serialized_start = 2054
    _DELEGATIONDELEGATORREWARD._serialized_end = 2247
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._serialized_start = 2250
    _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._serialized_end = 2490
# @@protoc_insertion_point(module_scope)
