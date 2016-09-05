Name:           ros-kinetic-rbcar-robot-control
Version:        1.0.4
Release:        1%{?dist}
Summary:        ROS rbcar_robot_control package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rbcar_robot_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-ackermann-msgs
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-robotnik-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-ackermann-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-robotnik-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf

%description
The rbcar_robot_control package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Sep 05 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.4-1
- Autogenerated by Bloom

* Fri Jul 15 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.4-0
- Autogenerated by Bloom

