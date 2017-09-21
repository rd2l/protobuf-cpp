{
	'targets': [
	{
		'target_name': 'protobuf-steam',
		'dependencies': [
			"protobuf",
		],
		'type': 'static_library',
		'include_dirs': [
			'steam',
		],
		'conditions': [
			['OS=="linux"', {
				'!cflags': [
				  '-Weverything',
				],
				'cflags': [
				  '-w',
				]
			}
		]],
		'sources': [
			'<!@pymod_do_main(glob-files steam/**/*.cc)',
			'<!@pymod_do_main(glob-files steam/**/*.h)',
		]
	},
	{
		'target_name': 'protobuf-dota',
		'dependencies': [
			"protobuf",
			"protobuf-steam",
		],
		'type': 'static_library',
		'include_dirs': [
			'dota',
		],
		'conditions': [
			['OS=="linux"', {
				'!cflags': [
				  '-Weverything',
				],
				'cflags': [
				  '-w',
				]
			}
		]],
		'sources': [
			'<!@pymod_do_main(glob-files dota/**/*.cc)',
			'<!@pymod_do_main(glob-files dota/**/*.h)',
		]
	},
	{
		'target_name': 'protobuf',
		 'all_dependent_settings': {
          'include_dirs': [
			'protobuf/src',
		  ],
        },
		'type': 'static_library',
		'include_dirs': [
			'protobuf/src',
		],
		
		'conditions': [
			['OS=="linux"', {
				'defines': [
					'HAVE_PTHREAD',
				],
				'!cflags': [
				  '-Weverything',
				],
				'cflags': [
				  '-w',
				  '-Wno-unused-parameter',
				]
			}]],
		'sources': [
		"protobuf/src/google/protobuf/stubs/atomicops_internals_x86_gcc.cc",
		"protobuf/src/google/protobuf/stubs/atomicops_internals_x86_msvc.cc",
		"protobuf/src/google/protobuf/stubs/bytestream.cc",
		"protobuf/src/google/protobuf/stubs/bytestream.h",
		"protobuf/src/google/protobuf/stubs/common.cc",
		"protobuf/src/google/protobuf/stubs/hash.h",
		"protobuf/src/google/protobuf/stubs/int128.cc",
		"protobuf/src/google/protobuf/stubs/int128.h",	"protobuf/src/google/protobuf/stubs/map_util.h",
		"protobuf/src/google/protobuf/stubs/mathutil.h",
		"protobuf/src/google/protobuf/stubs/once.cc",
		"protobuf/src/google/protobuf/stubs/shared_ptr.h",
		"protobuf/src/google/protobuf/stubs/status.cc",
		"protobuf/src/google/protobuf/stubs/status.h",
		"protobuf/src/google/protobuf/stubs/status_macros.h",
		"protobuf/src/google/protobuf/stubs/statusor.cc",
		"protobuf/src/google/protobuf/stubs/statusor.h",
		"protobuf/src/google/protobuf/stubs/stringpiece.cc",
		"protobuf/src/google/protobuf/stubs/stringpiece.h",
		"protobuf/src/google/protobuf/stubs/stringprintf.cc",
		"protobuf/src/google/protobuf/stubs/stringprintf.h",
		"protobuf/src/google/protobuf/stubs/structurally_valid.cc",
		"protobuf/src/google/protobuf/stubs/strutil.cc",
		"protobuf/src/google/protobuf/stubs/strutil.h",
		"protobuf/src/google/protobuf/stubs/time.cc",
		"protobuf/src/google/protobuf/stubs/time.h",
		"protobuf/src/google/protobuf/arena.cc",
		"protobuf/src/google/protobuf/arenastring.cc",
		"protobuf/src/google/protobuf/extension_set.cc",
		"protobuf/src/google/protobuf/generated_message_util.cc",
		"protobuf/src/google/protobuf/message_lite.cc",
		"protobuf/src/google/protobuf/repeated_field.cc",
		"protobuf/src/google/protobuf/wire_format_lite.cc",
		"protobuf/src/google/protobuf/io/coded_stream.cc",
		"protobuf/src/google/protobuf/io/coded_stream_inl.h",
		"protobuf/src/google/protobuf/io/zero_copy_stream.cc",
		"protobuf/src/google/protobuf/io/zero_copy_stream_impl_lite.cc",
		"protobuf/src/google/protobuf/any.pb.cc",
		"protobuf/src/google/protobuf/api.pb.cc",
		"protobuf/src/google/protobuf/stubs/mathlimits.cc",
		"protobuf/src/google/protobuf/stubs/mathlimits.h",
		"protobuf/src/google/protobuf/any.cc",
		"protobuf/src/google/protobuf/descriptor.cc",
		"protobuf/src/google/protobuf/descriptor_database.cc",
		"protobuf/src/google/protobuf/descriptor.pb.cc",
		"protobuf/src/google/protobuf/duration.pb.cc",
		"protobuf/src/google/protobuf/dynamic_message.cc",
		"protobuf/src/google/protobuf/empty.pb.cc",
		"protobuf/src/google/protobuf/extension_set_heavy.cc",
		"protobuf/src/google/protobuf/field_mask.pb.cc",
		"protobuf/src/google/protobuf/generated_message_reflection.cc",
		"protobuf/src/google/protobuf/map_field.cc",
		"protobuf/src/google/protobuf/message.cc",
		"protobuf/src/google/protobuf/reflection_internal.h",
		"protobuf/src/google/protobuf/reflection_ops.cc",
		"protobuf/src/google/protobuf/service.cc",
		"protobuf/src/google/protobuf/source_context.pb.cc",
		"protobuf/src/google/protobuf/struct.pb.cc",
		"protobuf/src/google/protobuf/stubs/substitute.cc",
		"protobuf/src/google/protobuf/stubs/substitute.h",
		"protobuf/src/google/protobuf/text_format.cc",
		"protobuf/src/google/protobuf/timestamp.pb.cc",
		"protobuf/src/google/protobuf/type.pb.cc",
		"protobuf/src/google/protobuf/unknown_field_set.cc",
		"protobuf/src/google/protobuf/wire_format.cc",
		"protobuf/src/google/protobuf/wrappers.pb.cc",
		"protobuf/src/google/protobuf/io/gzip_stream.cc",
		"protobuf/src/google/protobuf/io/printer.cc",
		"protobuf/src/google/protobuf/io/strtod.cc",
		"protobuf/src/google/protobuf/io/tokenizer.cc",
		"protobuf/src/google/protobuf/io/zero_copy_stream_impl.cc",
		"protobuf/src/google/protobuf/compiler/importer.cc",
		"protobuf/src/google/protobuf/compiler/parser.cc",
		"protobuf/src/google/protobuf/util/delimited_message_util.cc",
		"protobuf/src/google/protobuf/util/field_comparator.cc",
		"protobuf/src/google/protobuf/util/field_mask_util.cc",
		"protobuf/src/google/protobuf/util/internal/constants.h",
		"protobuf/src/google/protobuf/util/internal/datapiece.cc",
		"protobuf/src/google/protobuf/util/internal/datapiece.h",
		"protobuf/src/google/protobuf/util/internal/default_value_objectwriter.cc",
		"protobuf/src/google/protobuf/util/internal/default_value_objectwriter.h",
		"protobuf/src/google/protobuf/util/internal/error_listener.cc",
		"protobuf/src/google/protobuf/util/internal/error_listener.h",
		"protobuf/src/google/protobuf/util/internal/expecting_objectwriter.h",
		"protobuf/src/google/protobuf/util/internal/field_mask_utility.cc",
		"protobuf/src/google/protobuf/util/internal/field_mask_utility.h",
		"protobuf/src/google/protobuf/util/internal/json_escaping.cc",
		"protobuf/src/google/protobuf/util/internal/json_escaping.h",
		"protobuf/src/google/protobuf/util/internal/json_objectwriter.cc",
		"protobuf/src/google/protobuf/util/internal/json_objectwriter.h",
		"protobuf/src/google/protobuf/util/internal/json_stream_parser.cc",
		"protobuf/src/google/protobuf/util/internal/json_stream_parser.h",
		"protobuf/src/google/protobuf/util/internal/location_tracker.h",
		"protobuf/src/google/protobuf/util/internal/mock_error_listener.h",
		"protobuf/src/google/protobuf/util/internal/object_location_tracker.h",
		"protobuf/src/google/protobuf/util/internal/object_source.h",
		"protobuf/src/google/protobuf/util/internal/object_writer.cc",
		"protobuf/src/google/protobuf/util/internal/object_writer.h",
		"protobuf/src/google/protobuf/util/internal/protostream_objectsource.cc",
		"protobuf/src/google/protobuf/util/internal/protostream_objectsource.h",
		"protobuf/src/google/protobuf/util/internal/protostream_objectwriter.cc",
		"protobuf/src/google/protobuf/util/internal/protostream_objectwriter.h",
		"protobuf/src/google/protobuf/util/internal/proto_writer.cc",
		"protobuf/src/google/protobuf/util/internal/proto_writer.h",
		"protobuf/src/google/protobuf/util/internal/structured_objectwriter.h",
		"protobuf/src/google/protobuf/util/internal/type_info.cc",
		"protobuf/src/google/protobuf/util/internal/type_info.h",
		"protobuf/src/google/protobuf/util/internal/type_info_test_helper.cc",
		"protobuf/src/google/protobuf/util/internal/type_info_test_helper.h",
		"protobuf/src/google/protobuf/util/internal/utility.cc",
		"protobuf/src/google/protobuf/util/internal/utility.h",
		"protobuf/src/google/protobuf/util/json_util.cc",
		"protobuf/src/google/protobuf/util/message_differencer.cc",
		"protobuf/src/google/protobuf/util/time_util.cc",
		"protobuf/src/google/protobuf/util/type_resolver_util.cc",
		]
	},
	]
}
