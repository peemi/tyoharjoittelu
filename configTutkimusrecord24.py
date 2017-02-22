# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: reco -s RAW2DIGI,L1Reco,RECO,ALCA:@MinimumBias,USER:EventFilter/HcalRawToDigi/hcallaserhbhehffilter2012_cff.hcallLaser2012Filter,DQM:@MinimumBias --data --conditions FT_R_53_LV5::All --eventcontent RECO,AOD,DQM --datatier RECO,AOD,DQM --customise Configuration/DataProcessing/RecoTLR.customisePrompt --no_exec --python reco_2011A_MinimumBias.py

#tuodaan todennäköisesti CMSSW5.X:stä kirjasto tuo nimellä cms. Koska kirjasto on tuotu omalla nimellään kaikki funkion ja toiminnallisuuksie haut utlee tehdä cms reitin kautta.
import FWCore.ParameterSet.Config as cms

#haetaan lisää reitistä cms.process('RECO') lyhennetään tämä "reitti" parametriin process. Mitä tarkoittaa FWCore.ParameterSet.Config.Process('RECO')? Hain reitin CMS_5_3_X tuon reitin. Eroja: parametersetin ja configin välissä oli python ja config.pystä ei suoraan löytynyt mitään RECO nimistä. Mutta Process luokka löytyi, mikä auttaa jo paljon sillä luokassa saattaa olla jokin automaattifunktio joka hakee prosesseja ja tämä koodi haluaa käyttää prosessia nimeltä RECO. Mutta haluaisin silti löytää sen sillä kaikki näytetään tehtävän sen avulla.

#vai määritelläänkö/luodaanko tässä prosessi nimeltä reco johon haetaan parametrejä/confeja? 

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreams_cff')
process.load('EventFilter.HcalRawToDigi.hcallaserhbhehffilter2012_cff')
process.load('DQMOffline.Configuration.DQMOffline_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:reco_DIGI2RAW.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('reco nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RECOoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOEventContent.outputCommands,
    fileName = cms.untracked.string('reco_RAW2DIGI_L1Reco_RECO_ALCA_USER_DQM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RECO')
    )
)

process.AODoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODEventContent.outputCommands,
    fileName = cms.untracked.string('reco_RAW2DIGI_L1Reco_RECO_ALCA_USER_DQM_inAOD.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('AOD')
    )
)

process.DQMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.DQMEventContent.outputCommands,
    fileName = cms.untracked.string('reco_RAW2DIGI_L1Reco_RECO_ALCA_USER_DQM_inDQM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('DQM')
    )
)

# Additional output definition
process.ALCARECOStreamSiStripCalMinBias = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripCalMinBias')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOSiStripCalMinBias_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*'),
    fileName = cms.untracked.string('SiStripCalMinBias.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string('SiStripCalMinBias'),
        dataTier = cms.untracked.string('ALCARECO')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880)
)
process.ALCARECOStreamTkAlMinBias = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMinBias')
    ),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlMinBias_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_offlineBeamSpot_*_*'),
    fileName = cms.untracked.string('TkAlMinBias.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string('TkAlMinBias'),
        dataTier = cms.untracked.string('ALCARECO')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880)
)

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'FT_R_53_LV5::All', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.user_step = cms.Path(process.hcallLaser2012Filter)
process.dqmoffline_step = cms.Path(process.bTagPlots)
process.dqmoffline_1_step = cms.Path(process.HcalDQMOfflineSequence)
process.dqmoffline_2_step = cms.Path(process.egammaDQMOffline)
process.dqmoffline_3_step = cms.Path(process.DQMOfflineCommonSiStripZeroBias)
process.dqmoffline_4_step = cms.Path(process.DQMOfflineMuon)
process.dqmoffline_5_step = cms.Path(process.DQMOfflineHcal)
process.dqmoffline_6_step = cms.Path(process.DQMOfflineJetMET)
process.dqmoffline_7_step = cms.Path(process.DQMOfflineEcal)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)
process.AODoutput_step = cms.EndPath(process.AODoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)
process.ALCARECOStreamSiStripCalMinBiasOutPath = cms.EndPath(process.ALCARECOStreamSiStripCalMinBias)
process.ALCARECOStreamTkAlMinBiasOutPath = cms.EndPath(process.ALCARECOStreamTkAlMinBias)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.pathALCARECOSiStripCalMinBias,process.pathALCARECOTkAlMinBias,process.user_step,process.dqmoffline_step,process.dqmoffline_1_step,process.dqmoffline_2_step,process.dqmoffline_3_step,process.dqmoffline_4_step,process.dqmoffline_5_step,process.dqmoffline_6_step,process.dqmoffline_7_step,process.endjob_step,process.RECOoutput_step,process.AODoutput_step,process.DQMoutput_step,process.ALCARECOStreamSiStripCalMinBiasOutPath,process.ALCARECOStreamTkAlMinBiasOutPath)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.RecoTLR
from Configuration.DataProcessing.RecoTLR import customisePrompt 

#call to customisation function customisePrompt imported from Configuration.DataProcessing.RecoTLR
process = customisePrompt(process)

# End of customisation functions
