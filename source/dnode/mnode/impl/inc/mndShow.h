/*
 * Copyright (c) 2019 TAOS Data, Inc. <jhtao@taosdata.com>
 *
 * This program is free software: you can use, redistribute, and/or modify
 * it under the terms of the GNU Affero General Public License, version 3
 * or later ("AGPL"), as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef _TD_MND_SHOW_H_
#define _TD_MND_SHOW_H_

#include "mndInt.h"

#ifdef __cplusplus
extern "C" {
#endif

int32_t mndInitShow(SMnode *pMnode);
void    mndCleanupShow(SMnode *pMnode);
void    mndAddShowMetaHandle(SMnode *pMnode, EShowType showType, ShowMetaFp fp);
void    mndAddShowRetrieveHandle(SMnode *pMnode, EShowType showType, ShowRetrieveFp fp);
void    mndAddShowFreeIterHandle(SMnode *pMnode, EShowType msgType, ShowFreeIterFp fp);
void    mnodeVacuumResult(char *data, int32_t numOfCols, int32_t rows, int32_t capacity, SShowObj *pShow);
char   *mndShowStr(int32_t showType);

#ifdef __cplusplus
}
#endif

#endif /*_TD_MND_SHOW_H_*/
