#encoding=utf-8
INNODB_PAGE_SIZE = 16*1024*1024

# Start of the data on the page
FIL_PAGE_DATA = 38


FIL_PAGE_OFFSET = 4 # page offset inside space
FIL_PAGE_TYPE = 24 # File page type

# Types of an undo log segment */
TRX_UNDO_INSERT = 1
TRX_UNDO_UPDATE = 2

# On a page of any file segment, data may be put starting from this offset
FSEG_PAGE_DATA = FIL_PAGE_DATA

# The offset of the undo log page header on pages of the undo log
TRX_UNDO_PAGE_HDR = FSEG_PAGE_DATA

PAGE_LEVEL = 26	#level of the node in an index tree; the leaf level is the level 0 */

# MySQL8.0 File Page Types		
innodb_page_type={
	'0000':u'Freshly Allocated Page',
	'0001':u'Unused Page Type',
	'0002':u'Undo Log Page',
	'0003':u'Index Node',
	'0004':u'Insert Buffer Free List',
	'0005':u'Insert Buffer Bitmap',
	'0006':u'System Page',
	'0007':u'Transaction system Page',
	'0008':u'File Space Header',
	'0009':u'Extend Descriptor Page',
	'000a':u'Uncompressed BLOB Page',
	'000b':u'1st Compressed BLOB Page',
	'000c':u'Subsequent Compressed BLOB Page',
	'000e':u'Compressed Page',
	'000f':u'Encrypted Page',
	'0010':u'Compressed and Encrypted page',
	'0011':u'Encrypted R-tree Page',
	'0012':u'Uncompressed SDI BLOB Page',
	'0013':u'Commpressed SDI BLOB Page',
	'0014':u'Legacy Doublewrite Buffer Page',
	'0015':u'Rollback Segment Array Page',
	'0016':u'Index Pages of Uncompressed LOB',
	'0017':u'Data Pages of Uncompressed LOB',
	'0018':u'The First Page of an Uncompressed LOB',
	'0019':u'The First Page of a Compressed LOB',
	'001a':u'Data Pages of Compressed LOB',
	'001b':u'Index Pages of Compressed LOB.',
	'001c':u'Fragment Pages of Compressed LOB',
	'001d':u'Index Pages of Fragment Pages',
	'001e':u'Note the Higest Valid non-index page_type_t',
	'45bd':u'Tablespace SDI Index Page',
	'45be':u'R-tree Node',
	'45bf':u'B-tree Node'
	}
	
innodb_page_direction={
	'0000': 'Unknown(0x0000)',
	'0001': 'Page Left',
	'0002': 'Page Right',
	'0003': 'Page Same Rec',
	'0004': 'Page Same Page',
	'0005': 'Page No Direction',
	'ffff': 'Unkown2(0xffff)'
}


INNODB_PAGE_SIZE=1024*16 # InnoDB Page 16K