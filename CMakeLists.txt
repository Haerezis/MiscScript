cmake_minimum_required (VERSION 2.8)

# project name
set(PROJECT_NAME "")
project (${PROJECT_NAME})

# setup version numbers
set(VERSION_MAJOR 0)
set(VERSION_MINOR 2)
set(VERSION_PATCH 0)


add_definitions("-std=c++11")


set(INTERNAL_LIBS "")
set(EXTERNAL_LIBS "")
set(DEFINES "")
set(WARNING "")
set(FLAGS "")
set(CMAKE_CXX_FLAGS "${DEFINES} ${WARNING} ${FLAGS}")


set(OUTPUT_DIR "${CMAKE_CURRENT_SOURCE_DIR}/bin/")

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${OUTPUT_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${OUTPUT_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${OUTPUT_DIR})
set(LIB_INSTALL_DIR ${OUTPUT_DIR})
# Second, for multi-config builds (e.g. msvc)
foreach( OUTPUTCONFIG ${CMAKE_CONFIGURATION_TYPES} )
    string( TOUPPER ${OUTPUTCONFIG} OUTPUTCONFIG )
    set( CMAKE_RUNTIME_OUTPUT_DIRECTORY_${OUTPUTCONFIG} ${OUTPUT_DIR} )
    set( CMAKE_LIBRARY_OUTPUT_DIRECTORY_${OUTPUTCONFIG} ${OUTPUT_DIR} )
    set( CMAKE_ARCHIVE_OUTPUT_DIRECTORY_${OUTPUTCONFIG} ${OUTPUT_DIR} )
endforeach( OUTPUTCONFIG CMAKE_CONFIGURATION_TYPES )

set_option(BUILD_DOC TRUE BOOL "build the documentation (doxygen is require)")
set_option(BUILD_SAMPLES TRUE BOOL "build the samples")

#add_subdirectory
