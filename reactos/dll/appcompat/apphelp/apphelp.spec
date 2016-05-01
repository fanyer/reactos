@ stdcall AllowPermLayer(wstr)
@ stub ApphelpCheckExe
@ stdcall ApphelpCheckInstallShieldPackage(ptr wstr)
@ stub ApphelpCheckMsiPackage
@ stub ApphelpCheckRunApp
@ stub ApphelpCheckRunAppEx
@ stub ApphelpCheckShellObject
@ stub ApphelpCreateAppcompatData
@ stub ApphelpFixMsiPackage
@ stub ApphelpFixMsiPackageExe
@ stub ApphelpFreeFileAttributes
@ stub ApphelpGetFileAttributes
@ stub ApphelpGetMsiProperties
@ stub ApphelpGetNTVDMInfo
@ stub ApphelpParseModuleData
@ stub ApphelpQueryModuleData
@ stub ApphelpQueryModuleDataEx
@ stub ApphelpUpdateCacheEntry
@ stub GetPermLayers
@ stub SdbAddLayerTagRefToQuery
@ stub SdbApphelpNotify
@ stub SdbApphelpNotifyExSdbApphelpNotifyEx
@ stub SdbBeginWriteListTag
@ stub SdbBuildCompatEnvVariables
@ stub SdbCloseApphelpInformation
@ stub SdbCloseDatabase
@ stub SdbCloseDatabaseWrite
@ stub SdbCloseLocalDatabase
@ stub SdbCommitIndexes
@ stub SdbCreateDatabase
@ stub SdbCreateHelpCenterURL
@ stub SdbCreateMsiTransformFile
@ stub SdbDeclareIndex
@ stub SdbDumpSearchPathPartCaches
@ stub SdbEnumMsiTransforms
@ stub SdbEndWriteListTag
@ stub SdbEscapeApphelpURL
@ stub SdbFindFirstDWORDIndexedTag
@ stub SdbFindFirstMsiPackage
@ stub SdbFindFirstMsiPackage_Str
@ stub SdbFindFirstNamedTag
@ stub SdbFindFirstStringIndexedTag
@ stub SdbFindFirstTag
@ stub SdbFindFirstTagRef
@ stub SdbFindNextDWORDIndexedTag
@ stub SdbFindNextMsiPackage
@ stub SdbFindNextStringIndexedTag
@ stub SdbFindNextTag
@ stub SdbFindNextTagRef
@ stub SdbFreeDatabaseInformation
@ stdcall SdbFreeFileAttributes(ptr)
@ stub SdbFreeFileInfo
@ stub SdbFreeFlagInfo
@ stub SdbGetAppCompatDataSize
@ stub SdbGetAppPatchDir
@ stub SdbGetBinaryTagData
@ stub SdbGetDatabaseID
@ stub SdbGetDatabaseInformation
@ stub SdbGetDatabaseInformationByName
@ stub SdbGetDatabaseMatch
@ stub SdbGetDatabaseVersion
@ stub SdbGetDllPath
@ stub SdbGetEntryFlags
@ stdcall SdbGetFileAttributes(wstr ptr ptr)
@ stub SdbGetFileImageType
@ stub SdbGetFileImageTypeEx
@ stub SdbGetFileInfo
@ stub SdbGetFirstChild
@ stub SdbGetIndex
@ stub SdbGetItemFromItemRef
@ stub SdbGetLayerName
@ stub SdbGetLayerTagRef
@ stub SdbGetLocalPDB
@ stub SdbGetMatchingExe
@ stub SdbGetMsiPackageInformation
@ stub SdbGetNamedLayer
@ stub SdbGetNextChild
@ stub SdbGetNthUserSdb
@ stdcall SdbGetPermLayerKeys(wstr wstr ptr long)
@ stub SdbGetShowDebugInfoOption
@ stub SdbGetShowDebugInfoOptionValue
@ stdcall SdbGetStandardDatabaseGUID(long ptr)
@ stub SdbGetStringTagPtr
@ stub SdbGetTagDataSize
@ stub SdbGetTagFromTagID
@ stub SdbGrabMatchingInfo
@ stub SdbGrabMatchingInfoEx
@ stdcall SdbGUIDFromString(wstr ptr)
@ stdcall SdbGUIDToString(ptr wstr long)
@ stub SdbInitDatabase
@ stub SdbInitDatabaseEx
@ stdcall SdbIsNullGUID(ptr)
@ stub SdbIsStandardDatabase
@ stub SdbIsTagrefFromLocalDB
@ stub SdbIsTagrefFromMainDB
@ stub SdbLoadString
@ stub SdbMakeIndexKeyFromString
@ stub SdbOpenApphelpDetailsDatabase
@ stub SdbOpenApphelpDetailsDatabaseSP
@ stub SdbOpenApphelpInformation
@ stub SdbOpenApphelpInformationByID
@ stub SdbOpenApphelpResourceFile
@ stub SdbOpenDatabase
@ stub SdbOpenDbFromGuid
@ stub SdbOpenLocalDatabase
@ stub SdbPackAppCompatData
@ stub SdbQueryApphelpInformation
@ stub SdbQueryBlockUpgrade
@ stub SdbQueryContext
@ stub SdbQueryData
@ stub SdbQueryDataEx
@ stub SdbQueryDataExTagID
@ stub SdbQueryFlagInfo
@ stub SdbQueryName
@ stub SdbQueryReinstallUpgrade
@ stub SdbReadApphelpData
@ stub SdbReadApphelpDetailsData
@ stub SdbReadBinaryTag
@ stub SdbReadBYTETag
@ stub SdbReadDWORDTag
@ stub SdbReadDWORDTagRef
@ stub SdbReadEntryInformation
@ stub SdbReadMsiTransformInfo
@ stub SdbReadPatchBits
@ stub SdbReadQWORDTag
@ stub SdbReadQWORDTagRef
@ stub SdbReadStringTag
@ stub SdbReadStringTagRef
@ stub SdbReadWORDTag
@ stub SdbReadWORDTagRef
@ stub SdbRegisterDatabase
@ stub SdbReleaseDatabase
@ stub SdbReleaseMatchingExe
@ stub SdbResolveDatabase
@ stub SdbSetApphelpDebugParameters
@ stub SdbSetEntryFlags
@ stub SdbSetImageType
@ stdcall SdbSetPermLayerKeys(wstr wstr long)
@ stub SdbShowApphelpDialog
@ stub SdbShowApphelpFromQuery
@ stub SdbStartIndexing
@ stub SdbStopIndexing
@ stub SdbStringDuplicate
@ stub SdbStringReplace
@ stub SdbStringReplaceArray
@ stub SdbTagIDToTagRef
@ stub SdbTagRefToTagID
@ stdcall SdbTagToString(long)
@ stub SdbUnregisterDatabase
@ stub SdbWriteBinaryTag
@ stub SdbWriteBinaryTagFromFile
@ stub SdbWriteBYTETag
@ stub SdbWriteDWORDTag
@ stub SdbWriteNULLTag
@ stub SdbWriteQWORDTag
@ stub SdbWriteStringRefTag
@ stub SdbWriteStringTag
@ stub SdbWriteStringTagDirect
@ stub SdbWriteWORDTag
@ stub SE_DllLoaded
@ stub SE_DllUnloaded
@ stub SE_GetHookAPIs
@ stub SE_GetMaxShimCount
@ stub SE_GetProcAddressLoad
@ stub SE_GetShimCount
@ stub SE_InstallAfterInit
@ stub SE_InstallBeforeInit
@ stub SE_IsShimDll
@ stub SE_LdrEntryRemoved
@ stub SE_ProcessDying
@ stub SetPermLayers
@ cdecl ShimDbgPrint(long str str)
@ stub ShimDumpCache
@ stub ShimFlushCache
@ stdcall SetPermLayerState(wstr wstr long long long)
