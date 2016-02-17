{
  'targets': [
    {
      'includes': [ 'native_mate_files.gypi' ],
      'target_name': 'native_mate',
      'type': 'static_library',
      'defines': [
            'NOMINMAX',
      ],
      'include_dirs': [
        '..',
        '.',
        '../node/src',
        '../node/deps',
      ],
      'sources': [
        '<@(native_mate_files)',
      ],
      'dependencies': [
        '../base/base.gyp:base',
        '../v8/tools/gyp/v8.gyp:v8'
      ]
    },
  ],
}
