# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: price-service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='price-service.proto',
  package='priceServicePackage',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x13price-service.proto\x12\x13priceServicePackage\"A\n\nItemDetail\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\x12\x11\n\titem_name\x18\x02 \x01(\t\x12\x0f\n\x07shop_id\x18\x03 \x01(\x03\"9\n\tItemPrice\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\x12\r\n\x05price\x18\x02 \x01(\x05\x12\x0c\n\x04time\x18\x03 \x01(\x03\"+\n\x0cPriceLogItem\x12\r\n\x05price\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x03\"(\n\x15ReadItemDetailRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\"_\n\x16ReadItemDetailResponse\x12\x33\n\nitemDetail\x18\x01 \x01(\x0b\x32\x1f.priceServicePackage.ItemDetail\x12\x10\n\x08notFound\x18\x02 \x01(\x03\"&\n\x13ReadItemInfoRequest\x12\x0f\n\x07item_id\x18\x01 \x03(\x03\"M\n\x14ReadItemInfoResponse\x12\x35\n\x0citem_details\x18\x01 \x03(\x0b\x32\x1f.priceServicePackage.ItemDetail\"@\n\x1c\x43reateItemDetailPriceRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\x12\x0f\n\x07shop_id\x18\x02 \x01(\x03\"0\n\x1d\x43reateItemDetailPriceResponse\x12\x0f\n\x07success\x18\x01 \x01(\x03\")\n\x16ReadPriceChangeRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\"\\\n\x17ReadPriceChangeResponse\x12/\n\x04list\x18\x01 \x03(\x0b\x32!.priceServicePackage.PriceLogItem\x12\x10\n\x08notFound\x18\x02 \x01(\x03\x32\xcd\x03\n\x0cPriceService\x12j\n\x0fReadItemDetails\x12*.priceServicePackage.ReadItemDetailRequest\x1a+.priceServicePackage.ReadItemDetailResponse\x12~\n\x15\x43reateItemDetailPrice\x12\x31.priceServicePackage.CreateItemDetailPriceRequest\x1a\x32.priceServicePackage.CreateItemDetailPriceResponse\x12l\n\x0fReadPriceChange\x12+.priceServicePackage.ReadPriceChangeRequest\x1a,.priceServicePackage.ReadPriceChangeResponse\x12\x63\n\x0cReadItemInfo\x12(.priceServicePackage.ReadItemInfoRequest\x1a).priceServicePackage.ReadItemInfoResponseb\x06proto3'
)




_ITEMDETAIL = _descriptor.Descriptor(
  name='ItemDetail',
  full_name='priceServicePackage.ItemDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='priceServicePackage.ItemDetail.item_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_name', full_name='priceServicePackage.ItemDetail.item_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shop_id', full_name='priceServicePackage.ItemDetail.shop_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=109,
)


_ITEMPRICE = _descriptor.Descriptor(
  name='ItemPrice',
  full_name='priceServicePackage.ItemPrice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='priceServicePackage.ItemPrice.item_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='priceServicePackage.ItemPrice.price', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='priceServicePackage.ItemPrice.time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=168,
)


_PRICELOGITEM = _descriptor.Descriptor(
  name='PriceLogItem',
  full_name='priceServicePackage.PriceLogItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='priceServicePackage.PriceLogItem.price', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='priceServicePackage.PriceLogItem.time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=213,
)


_READITEMDETAILREQUEST = _descriptor.Descriptor(
  name='ReadItemDetailRequest',
  full_name='priceServicePackage.ReadItemDetailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='priceServicePackage.ReadItemDetailRequest.item_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=255,
)


_READITEMDETAILRESPONSE = _descriptor.Descriptor(
  name='ReadItemDetailResponse',
  full_name='priceServicePackage.ReadItemDetailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='itemDetail', full_name='priceServicePackage.ReadItemDetailResponse.itemDetail', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notFound', full_name='priceServicePackage.ReadItemDetailResponse.notFound', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=352,
)


_READITEMINFOREQUEST = _descriptor.Descriptor(
  name='ReadItemInfoRequest',
  full_name='priceServicePackage.ReadItemInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='priceServicePackage.ReadItemInfoRequest.item_id', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=392,
)


_READITEMINFORESPONSE = _descriptor.Descriptor(
  name='ReadItemInfoResponse',
  full_name='priceServicePackage.ReadItemInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_details', full_name='priceServicePackage.ReadItemInfoResponse.item_details', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=471,
)


_CREATEITEMDETAILPRICEREQUEST = _descriptor.Descriptor(
  name='CreateItemDetailPriceRequest',
  full_name='priceServicePackage.CreateItemDetailPriceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='priceServicePackage.CreateItemDetailPriceRequest.item_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shop_id', full_name='priceServicePackage.CreateItemDetailPriceRequest.shop_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=537,
)


_CREATEITEMDETAILPRICERESPONSE = _descriptor.Descriptor(
  name='CreateItemDetailPriceResponse',
  full_name='priceServicePackage.CreateItemDetailPriceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='priceServicePackage.CreateItemDetailPriceResponse.success', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=587,
)


_READPRICECHANGEREQUEST = _descriptor.Descriptor(
  name='ReadPriceChangeRequest',
  full_name='priceServicePackage.ReadPriceChangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='priceServicePackage.ReadPriceChangeRequest.item_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=589,
  serialized_end=630,
)


_READPRICECHANGERESPONSE = _descriptor.Descriptor(
  name='ReadPriceChangeResponse',
  full_name='priceServicePackage.ReadPriceChangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='priceServicePackage.ReadPriceChangeResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notFound', full_name='priceServicePackage.ReadPriceChangeResponse.notFound', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=632,
  serialized_end=724,
)

_READITEMDETAILRESPONSE.fields_by_name['itemDetail'].message_type = _ITEMDETAIL
_READITEMINFORESPONSE.fields_by_name['item_details'].message_type = _ITEMDETAIL
_READPRICECHANGERESPONSE.fields_by_name['list'].message_type = _PRICELOGITEM
DESCRIPTOR.message_types_by_name['ItemDetail'] = _ITEMDETAIL
DESCRIPTOR.message_types_by_name['ItemPrice'] = _ITEMPRICE
DESCRIPTOR.message_types_by_name['PriceLogItem'] = _PRICELOGITEM
DESCRIPTOR.message_types_by_name['ReadItemDetailRequest'] = _READITEMDETAILREQUEST
DESCRIPTOR.message_types_by_name['ReadItemDetailResponse'] = _READITEMDETAILRESPONSE
DESCRIPTOR.message_types_by_name['ReadItemInfoRequest'] = _READITEMINFOREQUEST
DESCRIPTOR.message_types_by_name['ReadItemInfoResponse'] = _READITEMINFORESPONSE
DESCRIPTOR.message_types_by_name['CreateItemDetailPriceRequest'] = _CREATEITEMDETAILPRICEREQUEST
DESCRIPTOR.message_types_by_name['CreateItemDetailPriceResponse'] = _CREATEITEMDETAILPRICERESPONSE
DESCRIPTOR.message_types_by_name['ReadPriceChangeRequest'] = _READPRICECHANGEREQUEST
DESCRIPTOR.message_types_by_name['ReadPriceChangeResponse'] = _READPRICECHANGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ItemDetail = _reflection.GeneratedProtocolMessageType('ItemDetail', (_message.Message,), {
  'DESCRIPTOR' : _ITEMDETAIL,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.ItemDetail)
  })
_sym_db.RegisterMessage(ItemDetail)

ItemPrice = _reflection.GeneratedProtocolMessageType('ItemPrice', (_message.Message,), {
  'DESCRIPTOR' : _ITEMPRICE,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.ItemPrice)
  })
_sym_db.RegisterMessage(ItemPrice)

PriceLogItem = _reflection.GeneratedProtocolMessageType('PriceLogItem', (_message.Message,), {
  'DESCRIPTOR' : _PRICELOGITEM,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.PriceLogItem)
  })
_sym_db.RegisterMessage(PriceLogItem)

ReadItemDetailRequest = _reflection.GeneratedProtocolMessageType('ReadItemDetailRequest', (_message.Message,), {
  'DESCRIPTOR' : _READITEMDETAILREQUEST,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.ReadItemDetailRequest)
  })
_sym_db.RegisterMessage(ReadItemDetailRequest)

ReadItemDetailResponse = _reflection.GeneratedProtocolMessageType('ReadItemDetailResponse', (_message.Message,), {
  'DESCRIPTOR' : _READITEMDETAILRESPONSE,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.ReadItemDetailResponse)
  })
_sym_db.RegisterMessage(ReadItemDetailResponse)

ReadItemInfoRequest = _reflection.GeneratedProtocolMessageType('ReadItemInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _READITEMINFOREQUEST,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.ReadItemInfoRequest)
  })
_sym_db.RegisterMessage(ReadItemInfoRequest)

ReadItemInfoResponse = _reflection.GeneratedProtocolMessageType('ReadItemInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _READITEMINFORESPONSE,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.ReadItemInfoResponse)
  })
_sym_db.RegisterMessage(ReadItemInfoResponse)

CreateItemDetailPriceRequest = _reflection.GeneratedProtocolMessageType('CreateItemDetailPriceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEITEMDETAILPRICEREQUEST,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.CreateItemDetailPriceRequest)
  })
_sym_db.RegisterMessage(CreateItemDetailPriceRequest)

CreateItemDetailPriceResponse = _reflection.GeneratedProtocolMessageType('CreateItemDetailPriceResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEITEMDETAILPRICERESPONSE,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.CreateItemDetailPriceResponse)
  })
_sym_db.RegisterMessage(CreateItemDetailPriceResponse)

ReadPriceChangeRequest = _reflection.GeneratedProtocolMessageType('ReadPriceChangeRequest', (_message.Message,), {
  'DESCRIPTOR' : _READPRICECHANGEREQUEST,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.ReadPriceChangeRequest)
  })
_sym_db.RegisterMessage(ReadPriceChangeRequest)

ReadPriceChangeResponse = _reflection.GeneratedProtocolMessageType('ReadPriceChangeResponse', (_message.Message,), {
  'DESCRIPTOR' : _READPRICECHANGERESPONSE,
  '__module__' : 'price_service_pb2'
  # @@protoc_insertion_point(class_scope:priceServicePackage.ReadPriceChangeResponse)
  })
_sym_db.RegisterMessage(ReadPriceChangeResponse)



_PRICESERVICE = _descriptor.ServiceDescriptor(
  name='PriceService',
  full_name='priceServicePackage.PriceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=727,
  serialized_end=1188,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReadItemDetails',
    full_name='priceServicePackage.PriceService.ReadItemDetails',
    index=0,
    containing_service=None,
    input_type=_READITEMDETAILREQUEST,
    output_type=_READITEMDETAILRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateItemDetailPrice',
    full_name='priceServicePackage.PriceService.CreateItemDetailPrice',
    index=1,
    containing_service=None,
    input_type=_CREATEITEMDETAILPRICEREQUEST,
    output_type=_CREATEITEMDETAILPRICERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadPriceChange',
    full_name='priceServicePackage.PriceService.ReadPriceChange',
    index=2,
    containing_service=None,
    input_type=_READPRICECHANGEREQUEST,
    output_type=_READPRICECHANGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadItemInfo',
    full_name='priceServicePackage.PriceService.ReadItemInfo',
    index=3,
    containing_service=None,
    input_type=_READITEMINFOREQUEST,
    output_type=_READITEMINFORESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRICESERVICE)

DESCRIPTOR.services_by_name['PriceService'] = _PRICESERVICE

# @@protoc_insertion_point(module_scope)
