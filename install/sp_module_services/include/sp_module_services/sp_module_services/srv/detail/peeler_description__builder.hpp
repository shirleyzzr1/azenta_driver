// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sp_module_services:srv/PeelerDescription.idl
// generated code does not contain a copyright notice

#ifndef SP_MODULE_SERVICES__SRV__DETAIL__PEELER_DESCRIPTION__BUILDER_HPP_
#define SP_MODULE_SERVICES__SRV__DETAIL__PEELER_DESCRIPTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sp_module_services/srv/detail/peeler_description__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sp_module_services
{

namespace srv
{

namespace builder
{

class Init_PeelerDescription_Request_description_request
{
public:
  Init_PeelerDescription_Request_description_request()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sp_module_services::srv::PeelerDescription_Request description_request(::sp_module_services::srv::PeelerDescription_Request::_description_request_type arg)
  {
    msg_.description_request = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sp_module_services::srv::PeelerDescription_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sp_module_services::srv::PeelerDescription_Request>()
{
  return sp_module_services::srv::builder::Init_PeelerDescription_Request_description_request();
}

}  // namespace sp_module_services


namespace sp_module_services
{

namespace srv
{

namespace builder
{

class Init_PeelerDescription_Response_description_response
{
public:
  Init_PeelerDescription_Response_description_response()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sp_module_services::srv::PeelerDescription_Response description_response(::sp_module_services::srv::PeelerDescription_Response::_description_response_type arg)
  {
    msg_.description_response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sp_module_services::srv::PeelerDescription_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sp_module_services::srv::PeelerDescription_Response>()
{
  return sp_module_services::srv::builder::Init_PeelerDescription_Response_description_response();
}

}  // namespace sp_module_services

#endif  // SP_MODULE_SERVICES__SRV__DETAIL__PEELER_DESCRIPTION__BUILDER_HPP_
