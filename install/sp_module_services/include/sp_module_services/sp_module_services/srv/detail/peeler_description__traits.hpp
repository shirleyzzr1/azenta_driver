// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sp_module_services:srv/PeelerDescription.idl
// generated code does not contain a copyright notice

#ifndef SP_MODULE_SERVICES__SRV__DETAIL__PEELER_DESCRIPTION__TRAITS_HPP_
#define SP_MODULE_SERVICES__SRV__DETAIL__PEELER_DESCRIPTION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sp_module_services/srv/detail/peeler_description__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sp_module_services
{

namespace srv
{

inline void to_flow_style_yaml(
  const PeelerDescription_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: description_request
  {
    out << "description_request: ";
    rosidl_generator_traits::value_to_yaml(msg.description_request, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PeelerDescription_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: description_request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "description_request: ";
    rosidl_generator_traits::value_to_yaml(msg.description_request, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PeelerDescription_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace sp_module_services

namespace rosidl_generator_traits
{

[[deprecated("use sp_module_services::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sp_module_services::srv::PeelerDescription_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  sp_module_services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sp_module_services::srv::to_yaml() instead")]]
inline std::string to_yaml(const sp_module_services::srv::PeelerDescription_Request & msg)
{
  return sp_module_services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sp_module_services::srv::PeelerDescription_Request>()
{
  return "sp_module_services::srv::PeelerDescription_Request";
}

template<>
inline const char * name<sp_module_services::srv::PeelerDescription_Request>()
{
  return "sp_module_services/srv/PeelerDescription_Request";
}

template<>
struct has_fixed_size<sp_module_services::srv::PeelerDescription_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sp_module_services::srv::PeelerDescription_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sp_module_services::srv::PeelerDescription_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace sp_module_services
{

namespace srv
{

inline void to_flow_style_yaml(
  const PeelerDescription_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: description_response
  {
    if (msg.description_response.size() == 0) {
      out << "description_response: []";
    } else {
      out << "description_response: [";
      size_t pending_items = msg.description_response.size();
      for (auto item : msg.description_response) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PeelerDescription_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: description_response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.description_response.size() == 0) {
      out << "description_response: []\n";
    } else {
      out << "description_response:\n";
      for (auto item : msg.description_response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PeelerDescription_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace sp_module_services

namespace rosidl_generator_traits
{

[[deprecated("use sp_module_services::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sp_module_services::srv::PeelerDescription_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  sp_module_services::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sp_module_services::srv::to_yaml() instead")]]
inline std::string to_yaml(const sp_module_services::srv::PeelerDescription_Response & msg)
{
  return sp_module_services::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sp_module_services::srv::PeelerDescription_Response>()
{
  return "sp_module_services::srv::PeelerDescription_Response";
}

template<>
inline const char * name<sp_module_services::srv::PeelerDescription_Response>()
{
  return "sp_module_services/srv/PeelerDescription_Response";
}

template<>
struct has_fixed_size<sp_module_services::srv::PeelerDescription_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sp_module_services::srv::PeelerDescription_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sp_module_services::srv::PeelerDescription_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<sp_module_services::srv::PeelerDescription>()
{
  return "sp_module_services::srv::PeelerDescription";
}

template<>
inline const char * name<sp_module_services::srv::PeelerDescription>()
{
  return "sp_module_services/srv/PeelerDescription";
}

template<>
struct has_fixed_size<sp_module_services::srv::PeelerDescription>
  : std::integral_constant<
    bool,
    has_fixed_size<sp_module_services::srv::PeelerDescription_Request>::value &&
    has_fixed_size<sp_module_services::srv::PeelerDescription_Response>::value
  >
{
};

template<>
struct has_bounded_size<sp_module_services::srv::PeelerDescription>
  : std::integral_constant<
    bool,
    has_bounded_size<sp_module_services::srv::PeelerDescription_Request>::value &&
    has_bounded_size<sp_module_services::srv::PeelerDescription_Response>::value
  >
{
};

template<>
struct is_service<sp_module_services::srv::PeelerDescription>
  : std::true_type
{
};

template<>
struct is_service_request<sp_module_services::srv::PeelerDescription_Request>
  : std::true_type
{
};

template<>
struct is_service_response<sp_module_services::srv::PeelerDescription_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SP_MODULE_SERVICES__SRV__DETAIL__PEELER_DESCRIPTION__TRAITS_HPP_
