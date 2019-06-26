# -*- coding: utf-8 -*-
"""
Created by Serino at 03/21/2018
"""
import youtube_dl

URL = input("Download URL >>")
youtube_dl.YoutubeDL(URL)
