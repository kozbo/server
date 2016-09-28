# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/bio_metadata_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh import bio_metadata_pb2 as ga4gh_dot_bio__metadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/bio_metadata_service.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n ga4gh/bio_metadata_service.proto\x12\x05ga4gh\x1a\x18ga4gh/bio_metadata.proto\"c\n\x18SearchIndividualsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\"-\n\x14GetIndividualRequest\x12\x15\n\rindividual_id\x18\x01 \x01(\t\"+\n\x13GetBiosampleRequest\x12\x14\n\x0c\x62iosample_id\x18\x01 \x01(\t\"\\\n\x19SearchIndividualsResponse\x12&\n\x0bindividuals\x18\x01 \x03(\x0b\x32\x11.ga4gh.Individual\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"y\n\x17SearchBiosamplesRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rindividual_id\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"Y\n\x18SearchBiosamplesResponse\x12$\n\nbiosamples\x18\x01 \x03(\x0b\x32\x10.ga4gh.Biosample\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xc0\x02\n\x12\x42ioMetadataService\x12V\n\x11SearchIndividuals\x12\x1f.ga4gh.SearchIndividualsRequest\x1a .ga4gh.SearchIndividualsResponse\x12S\n\x10SearchBiosamples\x12\x1e.ga4gh.SearchBiosamplesRequest\x1a\x1f.ga4gh.SearchBiosamplesResponse\x12?\n\rGetIndividual\x12\x1b.ga4gh.GetIndividualRequest\x1a\x11.ga4gh.Individual\x12<\n\x0cGetBiosample\x12\x1a.ga4gh.GetBiosampleRequest\x1a\x10.ga4gh.Biosampleb\x06proto3')
  ,
  dependencies=[ga4gh_dot_bio__metadata__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHINDIVIDUALSREQUEST = _descriptor.Descriptor(
  name='SearchIndividualsRequest',
  full_name='ga4gh.SearchIndividualsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.SearchIndividualsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.SearchIndividualsRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchIndividualsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchIndividualsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=168,
)


_GETINDIVIDUALREQUEST = _descriptor.Descriptor(
  name='GetIndividualRequest',
  full_name='ga4gh.GetIndividualRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='ga4gh.GetIndividualRequest.individual_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=215,
)


_GETBIOSAMPLEREQUEST = _descriptor.Descriptor(
  name='GetBiosampleRequest',
  full_name='ga4gh.GetBiosampleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='ga4gh.GetBiosampleRequest.biosample_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=260,
)


_SEARCHINDIVIDUALSRESPONSE = _descriptor.Descriptor(
  name='SearchIndividualsResponse',
  full_name='ga4gh.SearchIndividualsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individuals', full_name='ga4gh.SearchIndividualsResponse.individuals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchIndividualsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=354,
)


_SEARCHBIOSAMPLESREQUEST = _descriptor.Descriptor(
  name='SearchBiosamplesRequest',
  full_name='ga4gh.SearchBiosamplesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.SearchBiosamplesRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.SearchBiosamplesRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='ga4gh.SearchBiosamplesRequest.individual_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchBiosamplesRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchBiosamplesRequest.page_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=477,
)


_SEARCHBIOSAMPLESRESPONSE = _descriptor.Descriptor(
  name='SearchBiosamplesResponse',
  full_name='ga4gh.SearchBiosamplesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='biosamples', full_name='ga4gh.SearchBiosamplesResponse.biosamples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchBiosamplesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=479,
  serialized_end=568,
)

_SEARCHINDIVIDUALSRESPONSE.fields_by_name['individuals'].message_type = ga4gh_dot_bio__metadata__pb2._INDIVIDUAL
_SEARCHBIOSAMPLESRESPONSE.fields_by_name['biosamples'].message_type = ga4gh_dot_bio__metadata__pb2._BIOSAMPLE
DESCRIPTOR.message_types_by_name['SearchIndividualsRequest'] = _SEARCHINDIVIDUALSREQUEST
DESCRIPTOR.message_types_by_name['GetIndividualRequest'] = _GETINDIVIDUALREQUEST
DESCRIPTOR.message_types_by_name['GetBiosampleRequest'] = _GETBIOSAMPLEREQUEST
DESCRIPTOR.message_types_by_name['SearchIndividualsResponse'] = _SEARCHINDIVIDUALSRESPONSE
DESCRIPTOR.message_types_by_name['SearchBiosamplesRequest'] = _SEARCHBIOSAMPLESREQUEST
DESCRIPTOR.message_types_by_name['SearchBiosamplesResponse'] = _SEARCHBIOSAMPLESRESPONSE

SearchIndividualsRequest = _reflection.GeneratedProtocolMessageType('SearchIndividualsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHINDIVIDUALSREQUEST,
  __module__ = 'ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchIndividualsRequest)
  ))
_sym_db.RegisterMessage(SearchIndividualsRequest)

GetIndividualRequest = _reflection.GeneratedProtocolMessageType('GetIndividualRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETINDIVIDUALREQUEST,
  __module__ = 'ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.GetIndividualRequest)
  ))
_sym_db.RegisterMessage(GetIndividualRequest)

GetBiosampleRequest = _reflection.GeneratedProtocolMessageType('GetBiosampleRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBIOSAMPLEREQUEST,
  __module__ = 'ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.GetBiosampleRequest)
  ))
_sym_db.RegisterMessage(GetBiosampleRequest)

SearchIndividualsResponse = _reflection.GeneratedProtocolMessageType('SearchIndividualsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHINDIVIDUALSRESPONSE,
  __module__ = 'ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchIndividualsResponse)
  ))
_sym_db.RegisterMessage(SearchIndividualsResponse)

SearchBiosamplesRequest = _reflection.GeneratedProtocolMessageType('SearchBiosamplesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBIOSAMPLESREQUEST,
  __module__ = 'ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchBiosamplesRequest)
  ))
_sym_db.RegisterMessage(SearchBiosamplesRequest)

SearchBiosamplesResponse = _reflection.GeneratedProtocolMessageType('SearchBiosamplesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBIOSAMPLESRESPONSE,
  __module__ = 'ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchBiosamplesResponse)
  ))
_sym_db.RegisterMessage(SearchBiosamplesResponse)


# @@protoc_insertion_point(module_scope)
