#Proect: Cleaning Algorithm
#Date  : 21/11/2014
#Author: Vishwa Nath Jha
#eMail : vishwanath.jha91@gmail.com
#Data  : Data Crawled from Websites

#last modified on 06/01/2015(dd/mm/yyyy)

#Reading the Data
data <- read.csv(file.choose(),header=TRUE,stringsAsFactors=FALSE)

#list of clothing material 
materials <- read.csv(file.choose(),header=TRUE,stringsAsFactors=FALSE)

#list of unique keywords in the library
keyLib <- read.csv(file.choose(),header= TRUE, stringsAsFactors=FALSE)

#Removing the columns from "materials" which aren't considered
material <- materials[,1]
material <- unique(material)
#Removing the columns from "Data" which aren't considered
rem<-c(2,7,8,10)
trainData<-data[,-rem]

#loading the libraries
library(dplyr)
library(tidyr)
library(tm)
library(NLP)
library(stringr)

#Functions which will be used later in the code

#returns string w/o leading or trailing whitespace
trim <- function (x) gsub("^\\s+|\\s+$", "", x)

#Returns the reversed string
strReverse<- function(x) sapply(lapply(strsplit(x, NULL), rev), paste, collapse="")


#remove non alpha non numeric characters without space
rplcConcat <- function(x) 
{
  name<- unlist(x)
  name <- str_replace_all(name, "[^[:alnum:]]", "")
  name <- tolower(name)
  return(name)
}

#remove non alpha non numeric characters with space
rplc <- function(x) 
{
  name<- unlist(x)
  name <- str_replace_all(name, "[^[:alnum:]]", " ")
  name <- tolower(name)
  return(name)
}

#Creating Additional Columns from Breadcrumbs
breadcrumb<-trainData$breadcrumbs
breadcrumb<- unlist(breadcrumb)

bc<-do.call(rbind, strsplit(breadcrumb, '>'))
bc<-as.data.frame(bc)

trainData<-cbind(trainData,bc)
trainData<-trainData[,-7]

names(trainData)[7]<-paste("bcl0")
names(trainData)[8]<-paste("bcl1")
names(trainData)[9]<-paste("bcl2")
names(trainData)[10]<-paste("bcl3")
names(trainData)[11]<-paste("bcl4")
names(trainData)[12]<-paste("bcl5")

#triming the extra space in new breadcrumbs variables
trainData$bcl0 <- trim(trainData$bcl0)
trainData$bcl1 <- trim(trainData$bcl1)
trainData$bcl2 <- trim(trainData$bcl2)
trainData$bcl3 <- trim(trainData$bcl3)
trainData$bcl4 <- trim(trainData$bcl4)
trainData$bcl5 <- trim(trainData$bcl5)

#Separating the rows with level 4 in breadcrumbs
#level3<-trainData[trainData$bcl3=="Home",]
#write.csv(level3,"level3withhome.csv",row.names=F)
#tblWithLevel3<-Data1[Data1$bcl3!="Home",]
#Separating the rows with level 5 in breadcrumbs
level4<-trainData[trainData$bcl4=="Home",]
write.csv(level4,"level4withhome.csv",row.names=F)
tblWithLevel4<-trainData[trainData$bcl4!="Home",]

#Separating the rows with level 6 in breadcrumbs
#level5<-trainData[trainData$bcl5=="Home",]
#write.csv(level5,"level5withhome.csv",row.names=F)
#tblWithLevel5<-trainData[trainData$bcl5!="Home",]

#substitute the data set which is appropriate
trainData<-tblWithLevel4
#Removing level 6 from trainData
trainData<- trainData[,-12]

#Missing Value Treatment for Category
trainData$category[trainData$category==""] <- NA

#Substituting NA with "nocat"
Keep<- is.na(trainData$category)
trainData$category[trainData$category=="NA"] <- "nocat"

#breaking Categories to create lcat0, lcat1,lcat2
#Data1$category <- rplcConcat(Data1$category)

Cat <-as.character(trainData$category)
Cat <- unlist(Cat)
Cat1<- strReverse(Cat)
Cat3<-do.call(rbind, strsplit(Cat1,'>'))
Cat4<- Cat3[,1]
Cat5<- strReverse(Cat4)

#trim whitespace from lcat0
Cat6 <- trim(Cat5)
#lcat0
Cat6<- as.data.frame(Cat5)
Cat7<- Cat3[,2]
Cat8<- strReverse(Cat7)
#trim whitespace from lcat1
Cat8 <- trim(Cat7)
Cat8<- strReverse(Cat8)

#lcat1
Cat9<- as.data.frame(Cat8)
Cat2<- cbind(Cat9,Cat6)
trainData<-cbind(trainData,Cat2)
#removing row.names column from the data frame
rownames(trainData)<- NULL
#Assigning column names to lcat & lcat1
names(trainData)[12]<-paste("lcat1")
names(trainData)[13]<-paste("lcat0")

#trainData$lcat1 <- rplc(trainData$lcat1)
#trainData$lcat0 <- rplc(trainData$lcat0)

trainData$lcat1 <- gsub("\\s+"," ",trainData$lcat1)
trainData$lcat0 <- gsub("\\s+"," ",trainData$lcat0)
trainData<-trainData[,-5]

#Remove StopWords from Name
name <-rplc(trainData$name)
name <- tolower(name)
brand <-rplc(unique(trainData$brand))
brand <- tolower(brand)

#Create name corpus
name.corpus<- Corpus(VectorSource(name))

#Convert to lower case
#name.corpus <- tm_map(name.corpus, tolower)

#clean up by removing stop words
name.corpus <- tm_map(name.corpus,removeWords, c(stopwords("english"),"unisex","kids","women","men","s","â",",","'","soft","pink","beige","multicolor","sand","tan","red","peach","orange","brown","black","blue","green","cyan","silver","grey","indigo","magenta","maroon","transparent","turquoise","violet","white","yellow"))

#remove extra whitespace
#name.corpus <- tm_map(name.corpus, stripWhitespace)

dataframe<-data.frame(text=unlist(sapply(name.corpus, `[`, "content")),stringsAsFactors=F)
trainData<- cbind(trainData,dataframe)
trainData$text <- trim(trainData$text)
rownames(trainData)<- NULL

#Remove extra whitespaces from dataframe column
trainData$text <- gsub("\\s+"," ",trainData$text)

#clean up by removing brands
trainData$text <- gsub(x = trainData$text, pattern = paste(brand, collapse = "|"), replacement = "")

#clean up by removing materials
trainData$text <- gsub(x = trainData$text, pattern = paste(material, collapse = "|"), replacement = "")

names(trainData)[13]<-paste("name")

#Remove Original Name column
trainData<- trainData[,-1]
trainData$name<-gsub("\\s+"," ",trainData$name)

#Extract fname, lname0, lname1, lname2, lname3
trainData$name <- trim(trainData$name)
trainData$fname <- word(trainData$name,1)
trainData$lname0<- word(trainData$name,-1)
trainData$lname1<-sub('.*?(\\w+)\\W+\\w+\\W*?$', '\\1', trainData$name)
trainData$lname2<-do.call(paste, c(trainData[c("lname1", "lname0")], sep = " "))
trainData$lcat1<- trim(trainData$lcat1)
trainData$lcat0<- trim(trainData$lcat0)


#Write trainData into a new file
write.csv(trainData, file = "TrainData.csv", row.names= FALSE)


#****************************Keyword EXtraction Part Begins***********************************

keyLib <- trim(keyLib)

keyLib<- as.data.frame(keyLib)

for (i in 1:10353){
  text<- trainData$name[i]
  for(j in 1:1965){
    key<- keyLib[j]
    trainData$keyword <- str_extract(text,"key")
  } 
}


















