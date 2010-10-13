from distutils.core import setup
from glob import glob

setup(name='dh-builddep-metapackage',
      version='0.1',
	  scripts=['dh-builddep-metapackage'],
	  author="Tom Parker",
	  author_email="palfrey@tevp.net",
	  data_files = [
		  ('share/dh-builddep-metapackage/template',['template/%s'%x for x in ("compat", "copyright", "rules")]),
		  ('share/dh-builddep-metapackage/template/source',['template/source/format'])
		  ]
      )
