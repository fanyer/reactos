/*
 *  ReactOS winfile
 *
 *  drivebar.c
 *
 *  Copyright (C) 2002  Robert Dickenson <robd@reactos.org>
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
 */

#ifdef _MSC_VER
#include "stdafx.h"
#else
#define WIN32_LEAN_AND_MEAN     // Exclude rarely-used stuff from Windows headers
#include <windows.h>
#include <commctrl.h>
#include <stdlib.h>
#include <malloc.h>
#include <memory.h>
#include <tchar.h>
#include <process.h>
#include <stdio.h>
#endif
    
#include "main.h"
#include "settings.h"
#include "framewnd.h"
#include "childwnd.h"


////////////////////////////////////////////////////////////////////////////////
// Global Variables:
//

void ConfigureDriveBar(HWND hDriveBar)
{
    static DWORD dwLogicalDrivesSaved;
    DWORD dwLogicalDrives = GetLogicalDrives();

    if (!hDriveBar) return;

    if (dwLogicalDrives != dwLogicalDrivesSaved) {
	    TBBUTTON drivebarBtn = {0, 0, TBSTATE_ENABLED, TBSTYLE_SEP};
    	int btn = 1;
	    PTSTR p;
        int count = SendMessage(hDriveBar, TB_BUTTONCOUNT, 0, 0);
        while (count) {
			SendMessage(hDriveBar, TB_DELETEBUTTON, (WPARAM)--count, 0);
        }
        count = SendMessage(Globals.hDriveCombo, CB_GETCOUNT, 0, 0);
        while (count) {
//			SendMessage(Globals.hDriveCombo, CB_DELETESTRING, (WPARAM)--count, 0);
        }
        SendMessage(Globals.hDriveCombo, CB_RESETCONTENT, 0, 0); 
 
        memset(Globals.drives, 0, BUFFER_LEN);
	    GetLogicalDriveStrings(BUFFER_LEN, Globals.drives);
    	drivebarBtn.fsStyle = TBSTYLE_BUTTON;
        drivebarBtn.idCommand = ID_DRIVE_FIRST;
		for (p = Globals.drives; *p;) {
			 // insert drive letter
			TCHAR b[3] = { tolower(*p) };
			SendMessage(hDriveBar, TB_ADDSTRING, 0, (LPARAM)b);
			switch(GetDriveType(p)) {
			case DRIVE_REMOVABLE:	drivebarBtn.iBitmap = 1;	break;
			case DRIVE_CDROM:		drivebarBtn.iBitmap = 3;	break;
			case DRIVE_REMOTE:		drivebarBtn.iBitmap = 4;	break;
			case DRIVE_RAMDISK:		drivebarBtn.iBitmap = 5;	break;
			default:/*DRIVE_FIXED*/	drivebarBtn.iBitmap = 2;
			}
			SendMessage(hDriveBar, TB_INSERTBUTTON, btn, (LPARAM)&drivebarBtn);
			drivebarBtn.idCommand++;
			drivebarBtn.iString++;
			while(*p++);
//
//			SendMessage(Globals.hDriveCombo, CB_INSERTSTRING, btn, (LPARAM)b);
//			SendMessage(Globals.hDriveCombo, CB_ADDSTRING, 0, (LPARAM)b);
//            SendMessage(Globals.hDriveCombo, WM_SETTEXT, 0, (LPARAM)lpszWord); 
//            SendMessage(Globals.hDriveCombo, CB_ADDSTRING, 0, (LPARAM)&b); 
//
            ++btn;
		}
        dwLogicalDrivesSaved = dwLogicalDrives;

//        SendMessage(Globals.hDriveCombo, CB_SHOWDROPDOWN, (WPARAM)TRUE, (LPARAM)0);
    }
#ifndef __GNUC__

            {
            COMBOBOXEXITEM cbei;
            int iCnt;

            typedef struct {
                int iImage;
                int iSelectedImage;
                int iIndent;
                LPTSTR pszText;
            } ITEMINFO, *PITEMINFO;

#define MAX_ITEMS 15

    ITEMINFO IInf[] = {
        { 0, 3,  0, _T("first")}, 
        { 1, 4,  1, _T("second")},
        { 2, 5,  2, _T("third")},
        { 0, 3,  0, _T("fourth")},
        { 1, 4,  1, _T("fifth")},
        { 2, 5,  2, _T("sixth")},
        { 0, 3,  0, _T("seventh")},
        { 1, 4,  1, _T("eighth")},
        { 2, 5,  2, _T("ninth")},
        { 0, 3,  0, _T("tenth")},
        { 1, 4,  1, _T("eleventh")},
        { 2, 5,  2, _T("twelfth")},
        { 0, 3,  0, _T("thirteenth")},
        { 1, 4,  1, _T("fourteenth")},
        { 2, 5,  2, _T("fifteenth")}
    };

            for (iCnt = 0; iCnt < MAX_ITEMS; iCnt++) {

            cbei.mask = CBEIF_TEXT | CBEIF_INDENT | CBEIF_IMAGE| CBEIF_SELECTEDIMAGE;
            cbei.iItem          = iCnt;
            cbei.pszText        = IInf[iCnt].pszText;
            cbei.cchTextMax     = sizeof(IInf[iCnt].pszText);
            cbei.iImage         = IInf[iCnt].iImage;
            cbei.iSelectedImage = IInf[iCnt].iSelectedImage;
            cbei.iIndent        = IInf[iCnt].iIndent;
            }


            SendMessage(Globals.hDriveCombo, CBEM_INSERTITEM, 0, (LPARAM)&cbei); 
            }
#endif    
}

void _GetFreeSpaceEx(void)
{
   BOOL fResult;
   TCHAR szDrive[MAX_PATH];
   ULARGE_INTEGER i64FreeBytesToCaller;
   ULARGE_INTEGER i64TotalBytes;
   ULARGE_INTEGER i64FreeBytes;

   fResult = GetDiskFreeSpaceEx(szDrive,
                (PULARGE_INTEGER)&i64FreeBytesToCaller,
                (PULARGE_INTEGER)&i64TotalBytes,
                (PULARGE_INTEGER)&i64FreeBytes);
}

