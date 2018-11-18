#!/usr/bin/env python
# coding=utf8
from plugins.bottle.bottle import SimpleTemplate

import os.path
import sys

WEBPAGE_DIR = 'templates/pages'
ROOT = '/'
LANGUAGES = ['en', 'sp']

# Use the -t flag if you want to compile for local tests
DEPLOY = not '-t' in sys.argv

class Compiler(object):

    # Function: Run
    # -------------
    # This function compiles all the html files (recursively)
    # from the templates dir into the current folder. Folder
    # hierarchy is preserved
    def run(self):
        webpageFilePaths = self.getWebpageFilePaths()
        for lang in LANGUAGES:
            self.makePath(lang)
            for webpage in webpageFilePaths:
                fromPath = os.path.join(WEBPAGE_DIR, webpage)
                toPath = os.path.join(lang, webpage)
                self.compileTemplate(webpage, fromPath, toPath, lang)

    #####################
    # Private Helpers
    #####################

    def compileTemplate(self, page, fromPath, toPath, lang):
        print(fromPath)
        # note: all pages are in language/page
        pathToRoot = '../'
        templateText = open(fromPath).read()
        data = {
            'pathToRoot':pathToRoot,
            'lang':lang,
            'langName':self.getLangName(lang),
            'page':page
        }
        compiledHtml = SimpleTemplate(templateText).render(data)
        self.makePath(toPath)
        fileName, fileExtension = os.path.splitext(fromPath)
        compiledHtml = compiledHtml.encode('utf8')
        open(toPath, 'wb').write(compiledHtml)

    def getLangName(self, lang):
        names = {
            'en':'English',
            'sp':'Español',
        }
        return names[lang]

    def makePath(self, path):
        dirPath = os.path.dirname(path)
        if dirPath == '': return
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        
    def getPathToRoot(self, relativePath):
        if DEPLOY:
            return ROOT
        return self.getRelPathToRoot(relativePath)

    def getRelPathToRoot(self, relativePath):
        dirs = self.splitDirs(relativePath)
        depth = len(dirs) - 1
        pathToRoot = ''
        for i in range(depth, 0, -1):
            curr = dirs[i]
            pathToRoot += '../'
        print relativePath, pathToRoot
        return pathToRoot

    def splitDirs(self, filePath):
        if filePath == '': return []
        rootPath, last = os.path.split(filePath)
        rootDirs = self.splitDirs(rootPath)
        rootDirs.append(last)
        return rootDirs

    def isTemplateFile(self, fileName):
        extension = os.path.splitext(fileName)[1]
        return extension == '.html'

    def getWebpageFilePaths(self):
        paths = []
        templateDirPath = WEBPAGE_DIR
        for fileName in os.listdir(templateDirPath):
            templateFilePath = os.path.join(templateDirPath, fileName)
            # if os.path.isdir(templateFilePath):
            #     childPaths = self.getTemplateFilePaths(filePath)
            #     for childPath in childPaths:
            #         paths.append(childPath)
            if self.isTemplateFile(fileName):
                paths.append(fileName)
        return paths


if __name__ == '__main__':
    Compiler().run()
