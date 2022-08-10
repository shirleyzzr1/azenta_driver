// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sp_module_services:srv/PeelerActions.idl
// generated code does not contain a copyright notice
#include "sp_module_services/srv/detail/peeler_actions__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `action_request`
#include "rosidl_runtime_c/string_functions.h"

bool
sp_module_services__srv__PeelerActions_Request__init(sp_module_services__srv__PeelerActions_Request * msg)
{
  if (!msg) {
    return false;
  }
  // action_request
  if (!rosidl_runtime_c__String__init(&msg->action_request)) {
    sp_module_services__srv__PeelerActions_Request__fini(msg);
    return false;
  }
  return true;
}

void
sp_module_services__srv__PeelerActions_Request__fini(sp_module_services__srv__PeelerActions_Request * msg)
{
  if (!msg) {
    return;
  }
  // action_request
  rosidl_runtime_c__String__fini(&msg->action_request);
}

bool
sp_module_services__srv__PeelerActions_Request__are_equal(const sp_module_services__srv__PeelerActions_Request * lhs, const sp_module_services__srv__PeelerActions_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // action_request
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->action_request), &(rhs->action_request)))
  {
    return false;
  }
  return true;
}

bool
sp_module_services__srv__PeelerActions_Request__copy(
  const sp_module_services__srv__PeelerActions_Request * input,
  sp_module_services__srv__PeelerActions_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // action_request
  if (!rosidl_runtime_c__String__copy(
      &(input->action_request), &(output->action_request)))
  {
    return false;
  }
  return true;
}

sp_module_services__srv__PeelerActions_Request *
sp_module_services__srv__PeelerActions_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sp_module_services__srv__PeelerActions_Request * msg = (sp_module_services__srv__PeelerActions_Request *)allocator.allocate(sizeof(sp_module_services__srv__PeelerActions_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sp_module_services__srv__PeelerActions_Request));
  bool success = sp_module_services__srv__PeelerActions_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sp_module_services__srv__PeelerActions_Request__destroy(sp_module_services__srv__PeelerActions_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sp_module_services__srv__PeelerActions_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sp_module_services__srv__PeelerActions_Request__Sequence__init(sp_module_services__srv__PeelerActions_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sp_module_services__srv__PeelerActions_Request * data = NULL;

  if (size) {
    data = (sp_module_services__srv__PeelerActions_Request *)allocator.zero_allocate(size, sizeof(sp_module_services__srv__PeelerActions_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sp_module_services__srv__PeelerActions_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sp_module_services__srv__PeelerActions_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
sp_module_services__srv__PeelerActions_Request__Sequence__fini(sp_module_services__srv__PeelerActions_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      sp_module_services__srv__PeelerActions_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

sp_module_services__srv__PeelerActions_Request__Sequence *
sp_module_services__srv__PeelerActions_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sp_module_services__srv__PeelerActions_Request__Sequence * array = (sp_module_services__srv__PeelerActions_Request__Sequence *)allocator.allocate(sizeof(sp_module_services__srv__PeelerActions_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sp_module_services__srv__PeelerActions_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sp_module_services__srv__PeelerActions_Request__Sequence__destroy(sp_module_services__srv__PeelerActions_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sp_module_services__srv__PeelerActions_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sp_module_services__srv__PeelerActions_Request__Sequence__are_equal(const sp_module_services__srv__PeelerActions_Request__Sequence * lhs, const sp_module_services__srv__PeelerActions_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sp_module_services__srv__PeelerActions_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sp_module_services__srv__PeelerActions_Request__Sequence__copy(
  const sp_module_services__srv__PeelerActions_Request__Sequence * input,
  sp_module_services__srv__PeelerActions_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sp_module_services__srv__PeelerActions_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sp_module_services__srv__PeelerActions_Request * data =
      (sp_module_services__srv__PeelerActions_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sp_module_services__srv__PeelerActions_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sp_module_services__srv__PeelerActions_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sp_module_services__srv__PeelerActions_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
sp_module_services__srv__PeelerActions_Response__init(sp_module_services__srv__PeelerActions_Response * msg)
{
  if (!msg) {
    return false;
  }
  // action_response
  return true;
}

void
sp_module_services__srv__PeelerActions_Response__fini(sp_module_services__srv__PeelerActions_Response * msg)
{
  if (!msg) {
    return;
  }
  // action_response
}

bool
sp_module_services__srv__PeelerActions_Response__are_equal(const sp_module_services__srv__PeelerActions_Response * lhs, const sp_module_services__srv__PeelerActions_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // action_response
  if (lhs->action_response != rhs->action_response) {
    return false;
  }
  return true;
}

bool
sp_module_services__srv__PeelerActions_Response__copy(
  const sp_module_services__srv__PeelerActions_Response * input,
  sp_module_services__srv__PeelerActions_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // action_response
  output->action_response = input->action_response;
  return true;
}

sp_module_services__srv__PeelerActions_Response *
sp_module_services__srv__PeelerActions_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sp_module_services__srv__PeelerActions_Response * msg = (sp_module_services__srv__PeelerActions_Response *)allocator.allocate(sizeof(sp_module_services__srv__PeelerActions_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sp_module_services__srv__PeelerActions_Response));
  bool success = sp_module_services__srv__PeelerActions_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sp_module_services__srv__PeelerActions_Response__destroy(sp_module_services__srv__PeelerActions_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sp_module_services__srv__PeelerActions_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sp_module_services__srv__PeelerActions_Response__Sequence__init(sp_module_services__srv__PeelerActions_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sp_module_services__srv__PeelerActions_Response * data = NULL;

  if (size) {
    data = (sp_module_services__srv__PeelerActions_Response *)allocator.zero_allocate(size, sizeof(sp_module_services__srv__PeelerActions_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sp_module_services__srv__PeelerActions_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sp_module_services__srv__PeelerActions_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
sp_module_services__srv__PeelerActions_Response__Sequence__fini(sp_module_services__srv__PeelerActions_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      sp_module_services__srv__PeelerActions_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

sp_module_services__srv__PeelerActions_Response__Sequence *
sp_module_services__srv__PeelerActions_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sp_module_services__srv__PeelerActions_Response__Sequence * array = (sp_module_services__srv__PeelerActions_Response__Sequence *)allocator.allocate(sizeof(sp_module_services__srv__PeelerActions_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sp_module_services__srv__PeelerActions_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sp_module_services__srv__PeelerActions_Response__Sequence__destroy(sp_module_services__srv__PeelerActions_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sp_module_services__srv__PeelerActions_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sp_module_services__srv__PeelerActions_Response__Sequence__are_equal(const sp_module_services__srv__PeelerActions_Response__Sequence * lhs, const sp_module_services__srv__PeelerActions_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sp_module_services__srv__PeelerActions_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sp_module_services__srv__PeelerActions_Response__Sequence__copy(
  const sp_module_services__srv__PeelerActions_Response__Sequence * input,
  sp_module_services__srv__PeelerActions_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sp_module_services__srv__PeelerActions_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sp_module_services__srv__PeelerActions_Response * data =
      (sp_module_services__srv__PeelerActions_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sp_module_services__srv__PeelerActions_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sp_module_services__srv__PeelerActions_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sp_module_services__srv__PeelerActions_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
