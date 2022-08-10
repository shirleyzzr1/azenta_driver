// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sp_module_services:srv/PeelerActions.idl
// generated code does not contain a copyright notice

#ifndef SP_MODULE_SERVICES__SRV__DETAIL__PEELER_ACTIONS__STRUCT_H_
#define SP_MODULE_SERVICES__SRV__DETAIL__PEELER_ACTIONS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'action_request'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/PeelerActions in the package sp_module_services.
typedef struct sp_module_services__srv__PeelerActions_Request
{
  rosidl_runtime_c__String action_request;
} sp_module_services__srv__PeelerActions_Request;

// Struct for a sequence of sp_module_services__srv__PeelerActions_Request.
typedef struct sp_module_services__srv__PeelerActions_Request__Sequence
{
  sp_module_services__srv__PeelerActions_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sp_module_services__srv__PeelerActions_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/PeelerActions in the package sp_module_services.
typedef struct sp_module_services__srv__PeelerActions_Response
{
  bool action_response;
} sp_module_services__srv__PeelerActions_Response;

// Struct for a sequence of sp_module_services__srv__PeelerActions_Response.
typedef struct sp_module_services__srv__PeelerActions_Response__Sequence
{
  sp_module_services__srv__PeelerActions_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sp_module_services__srv__PeelerActions_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SP_MODULE_SERVICES__SRV__DETAIL__PEELER_ACTIONS__STRUCT_H_
