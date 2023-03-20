/*
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2020, Locus Robotics
 *  Copyright (c) 2023, Metro Robots
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of the copyright holder nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 */

/* Author: David V. Lu!! */

#pragma once

#include <std_msgs/msg/color_rgba.hpp>
#include <color_util/types.hpp>

namespace color_util
{
// Turning off clang to keep the horizontal alignment of the methods
// clang-format off
color_util::ColorRGBA toFloat(const color_util::ColorRGBA24& int_color);
color_util::ColorHSVA toFloat(const color_util::ColorHSVA24& int_color);

color_util::ColorRGBA24 toInt(const color_util::ColorRGBA& float_color);
color_util::ColorHSVA24 toInt(const color_util::ColorHSVA& float_color);

color_util::ColorHSVA   changeColorspace(const color_util::ColorRGBA&   rgba);
color_util::ColorHSVA24 changeColorspace(const color_util::ColorRGBA24& rgba);
color_util::ColorRGBA   changeColorspace(const color_util::ColorHSVA&   hsva);
color_util::ColorRGBA24 changeColorspace(const color_util::ColorHSVA24& hsva);

std_msgs::msg::ColorRGBA toMsg(const color_util::ColorRGBA&   rgba);
std_msgs::msg::ColorRGBA toMsg(const color_util::ColorRGBA24& rgba);
std_msgs::msg::ColorRGBA toMsg(const color_util::ColorHSVA&   hsva);
std_msgs::msg::ColorRGBA toMsg(const color_util::ColorHSVA24& hsva);
// clang-format on
}  // namespace color_util
