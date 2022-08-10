// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sp_module_services:srv/PeelerDescription.idl
// generated code does not contain a copyright notice

#ifndef SP_MODULE_SERVICES__SRV__DETAIL__PEELER_DESCRIPTION__STRUCT_HPP_
#define SP_MODULE_SERVICES__SRV__DETAIL__PEELER_DESCRIPTION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sp_module_services__srv__PeelerDescription_Request __attribute__((deprecated))
#else
# define DEPRECATED__sp_module_services__srv__PeelerDescription_Request __declspec(deprecated)
#endif

namespace sp_module_services
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct PeelerDescription_Request_
{
  using Type = PeelerDescription_Request_<ContainerAllocator>;

  explicit PeelerDescription_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->description_request = "";
    }
  }

  explicit PeelerDescription_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : description_request(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->description_request = "";
    }
  }

  // field types and members
  using _description_request_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _description_request_type description_request;

  // setters for named parameter idiom
  Type & set__description_request(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->description_request = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sp_module_services__srv__PeelerDescription_Request
    std::shared_ptr<sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sp_module_services__srv__PeelerDescription_Request
    std::shared_ptr<sp_module_services::srv::PeelerDescription_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PeelerDescription_Request_ & other) const
  {
    if (this->description_request != other.description_request) {
      return false;
    }
    return true;
  }
  bool operator!=(const PeelerDescription_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PeelerDescription_Request_

// alias to use template instance with default allocator
using PeelerDescription_Request =
  sp_module_services::srv::PeelerDescription_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sp_module_services


#ifndef _WIN32
# define DEPRECATED__sp_module_services__srv__PeelerDescription_Response __attribute__((deprecated))
#else
# define DEPRECATED__sp_module_services__srv__PeelerDescription_Response __declspec(deprecated)
#endif

namespace sp_module_services
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct PeelerDescription_Response_
{
  using Type = PeelerDescription_Response_<ContainerAllocator>;

  explicit PeelerDescription_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit PeelerDescription_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _description_response_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _description_response_type description_response;

  // setters for named parameter idiom
  Type & set__description_response(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->description_response = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sp_module_services__srv__PeelerDescription_Response
    std::shared_ptr<sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sp_module_services__srv__PeelerDescription_Response
    std::shared_ptr<sp_module_services::srv::PeelerDescription_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PeelerDescription_Response_ & other) const
  {
    if (this->description_response != other.description_response) {
      return false;
    }
    return true;
  }
  bool operator!=(const PeelerDescription_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PeelerDescription_Response_

// alias to use template instance with default allocator
using PeelerDescription_Response =
  sp_module_services::srv::PeelerDescription_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sp_module_services

namespace sp_module_services
{

namespace srv
{

struct PeelerDescription
{
  using Request = sp_module_services::srv::PeelerDescription_Request;
  using Response = sp_module_services::srv::PeelerDescription_Response;
};

}  // namespace srv

}  // namespace sp_module_services

#endif  // SP_MODULE_SERVICES__SRV__DETAIL__PEELER_DESCRIPTION__STRUCT_HPP_
