project(poppler)

set(poppler_SRC
    ${CMAKE_CURRENT_BINARY_DIR}/poppler/poppler_module_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/poppler/poppler_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/poppler/poppler_document_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/poppler/poppler_page_wrapper.cpp
)

set(poppler_INCLUDE_DIRECTORIES
    ${SHIBOKEN_INCLUDE_DIR}
    ${PYTHON_INCLUDE_PATH}
    ${PYSIDE_INCLUDE_DIR}
    ${PYSIDE_INCLUDE_DIR}/QtCore
    ${PYSIDE_INCLUDE_DIR}/QtGui
    ${QT_INCLUDE_DIR}
    ${QT_QTCORE_INCLUDE_DIR}
    ${POPPLER_QT4_INCLUDE_DIR}
)

set(poppler_LINK_LIBRARIES
    ${QT_QTCORE_LIBRARY}
    ${SHIBOKEN_PYTHON_LIBRARIES}
    ${SHIBOKEN_LIBRARY}
    ${PYSIDE_LIBRARY}
    ${POPPLER_QT4_LIBRARIES}
)

include_directories(poppler ${poppler_INCLUDE_DIRECTORIES})
add_library(poppler MODULE ${poppler_SRC})
set_property(TARGET poppler PROPERTY PREFIX "pyside_")
target_link_libraries(poppler ${poppler_LINK_LIBRARIES})

add_custom_command(OUTPUT ${poppler_SRC}
                   COMMAND ${GENERATOR} --enable-parent-ctor-heuristic --enable-pyside-extensions --enable-return-value-heuristic
                   ${CMAKE_SOURCE_DIR}/poppler/global.h
                   --include-paths=${QT_INCLUDE_DIR}:${POPPLER_QT4_INCLUDE_DIR}
                   --typesystem-paths=${typesystem_path}:${PYSIDE_TYPESYSTEMS}
                   --output-directory=${CMAKE_CURRENT_BINARY_DIR}
                   ${CMAKE_CURRENT_SOURCE_DIR}/typesystem_poppler.xml
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                   COMMENT "Running generator for libpoppler..."
                  )

