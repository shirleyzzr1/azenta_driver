// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sp_module_services:srv/PeelerActions.idl
// generated code does not contain a copyright notice

#ifndef SP_MODULE_SERVICES__SRV__DETAIL__PEELER_ACTIONS__BUILDER_HPP_
#define SP_MODULE_SERVICES__SRV__DETAIL__PEELER_ACTIONS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sp_module_services/srv/detail/peeler_actions__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sp_module_services
{

namespace srv
{

namespace builder
{

class Init_PeelerActions_Request_action_request
{
public:
  Init_PeelerActions_Request_action_request()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sp_module_services::srv::PeelerActions_Request action_request(::sp_module_services::srv::PeelerActions_Request::_action_request_type arg)
  {
    msg_.action_request = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sp_module_services::srv::PeelerActions_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sp_module_services::srv::PeelerActions_Request>()
{
  return sp_module_services::srv::builder::Init_PeelerActions_Request_action_request();
}

}  // namespace sp_module_services


namespace sp_module_services
{

namespace srv
{

namespace builder
{

class Init_PeelerActions_Response_action_response
{
public:
  Init_PeelerActions_Response_action_response()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sp_module_services::srv::PeelerActions_Response action_response(::sp_module_services::srv::PeelerActions_Response::_action_response_type arg)
  {
    msg_.action_response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sp_module_services::srv::PeelerActions_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sp_module_services::srv::PeelerActions_Response>()
{
  return sp_module_services::srv::builder::Init_PeelerActions_Response_action_response();
}

}  // namespace sp_module_services

#endif  // SP_MODULE_SERVICES__SRV__DETAIL__PEELER_ACTIONS__BUILDER_HPP_
