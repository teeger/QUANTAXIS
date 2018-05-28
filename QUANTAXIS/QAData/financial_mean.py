# coding:utf-8

financial_dict = {
    ## 每股指标
    '基本每股收益': 'EPS',
    '扣除非经常性损益每股收益': 'deductEPS',
    '每股未分配利润': 'undistributedProfitPerShare',
    '每股净资产': 'netAssetsPerShare',
    '每股资本公积金': 'capitalReservePerShare',
    '净资产收益率': 'ROE',
    '每股经营现金流量': 'operatingCashFlowPerShare',
    ## 资产负债表
    ### 资产
    #### 流动资产
    '货币资金': 'moneyFunds',
    '交易性金融资产': 'tradingFinancialAssets',
    '应收票据': 'billsReceivables',
    '应收账款': 'accountsReceivables',
    '预付款项': 'Prepayments',
    '其他应收款': 'otherReceivables',
    '应收关联公司款': 'interCompanyReceivables',
    '应收利息': 'interestReceivables',
    '应收股利': 'dividendsReceivables',
    '存货': 'inventory',
    '其中：消耗性生物资产': 'expendableBiologicalAssets',
    '一年内到期的非流动资产': 'noncurrentAssetsDueWithinOneYear',
    '其他流动资产': 'otherLiquidAssets',
    '流动资产合计': 'totalLiquidAssets',
    #### 非流动资产
    '可供出售金融资产': 'availableForSaleSecurities',
    '持有至到期投资': 'heldToMaturityInvestments',
    '长期应收款': 'longTermReceivables',
    '长期股权投资': 'longTermEquityInvestment',
    '投资性房地产': 'investmentRealEstate',
    '固定资产': 'fixedAssets',
    '在建工程': 'constructionInProgress',
    '工程物资': 'engineerMaterial',
    '固定资产清理': 'fixedAssetsCleanUp',
    '生产性生物资产': 'productiveBiologicalAssets',
    '油气资产': 'oilAndGasAssets',
    '无形资产': 'intangibleAssets',
    '开发支出': 'developmentExpenditure',
    '商誉': 'goodwill',
    '长期待摊费用': 'longTermDeferredExpenses',
    '递延所得税资产': 'deferredIncomeTaxAssets',
    '其他非流动资产': 'otherNonCurrentAssets',
    '非流动资产合计': 'totalNonCurrentAssets',
    '资产总计': 'totalAssets',
    ### 负债
    #### 流动负债
    '短期借款': 'shortTermLoan',
    '交易性金融负债': 'tradingFinancialLiabilities',
    '应付票据': 'billsPayable',
    '应付账款': 'accountsPayable',
    '预收款项': 'advancedReceivable',
    '应付职工薪酬': 'employeesPayable',
    '应交税费': 'taxPayable',
    '应付利息': 'interestPayable',
    '应付股利': 'dividendPayable',
    '其他应付款': 'otherPayable',
    '应付关联公司款': 'interCompanyPayable',
    '一年内到期的非流动负债': 'noncurrentLiabilitiesDueWithinOneYear',
    '其他流动负债': 'otherCurrentLiabilities',
    '流动负债合计': 'totalCurrentLiabilities',
    #### 非流动负债
    '长期借款': 'longTermLoans',
    '应付债券': 'bondsPayable',
    '长期应付款': 'longTermPayable',
    '专项应付款': 'specialPayable',
    '预计负债': 'estimatedLiabilities',
    '递延所得税负债': 'defferredIncomeTaxLiabilities',
    '其他非流动负债': 'otherNonCurrentLiabilities',
    '非流动负债合计': 'totalNonCurrentLiabilities',
    '负债合计': 'totalLiabilities',
    ### 所有者权益
    '实收资本（或股本）': 'totalShare',
    '资本公积': 'capitalReserve',
    '盈余公积': 'surplusReserve',
    '减：库存股': 'treasuryStock',
    '未分配利润': 'undistributedProfits',
    '少数股东权益': 'minorityEquity',
    '外币报表折算价差': 'foreignCurrencyReportTranslationSpread',
    '非正常经营项目收益调整': 'abnormalBusinessProjectEarningsAdjustment',
    '所有者权益（或股东权益）合计': 'totalOwnersEquity',
    '负债和所有者（或股东权益）合计': 'totalLiabilitiesAndOwnersEquity',
    ## 利润表
    '其中：营业收入': 'operatingRevenue',
    '其中：营业成本': 'operatingCosts',
    '营业税金及附加': 'taxAndSurcharges',
    '销售费用': 'salesCosts',
    '管理费用': 'managementCosts',
    '堪探费用': 'explorationCosts',
    '财务费用': 'financialCosts',
    '资产减值损失': 'assestsDevaluation',
    '加：公允价值变动净收益': 'profitAndLossFromFairValueChanges',
    '投资收益': 'investmentIncome',
    '其中：对联营企业和合营企业的投资收益': 'investmentIncomeFromAffiliatedBusinessAndCooperativeEnterprise',
    '影响营业利润的其他科目': 'otherSubjectsAffectingOperatingProfit',
    '三、营业利润': 'operatingProfit',
    '加：补贴收入': 'subsidyIncome',
    '营业外收入': 'nonOperatingIncome',
    '减：营业外支出': 'nonOperatingExpenses',
    '其中：非流动资产处置净损失': 'netLossFromDisposalOfNonCurrentAssets',
    '加：影响利润总额的其他科目': 'otherSubjectsAffectTotalProfit',
    '四、利润总额': 'totalProfit',
    '减：所得税': 'incomeTax',
    '加：影响净利润的其他科目': 'otherSubjectsAffectNetProfit',
    '五、净利润': 'netProfit',
    '归属于母公司所有者的净利润': 'netProfitsBelongToParentCompanyOwner',
    '少数股东损益': 'minorityProfitAndLoss',

    ## 现金流量表
    ### 经营活动 Operating
    '销售商品、提供劳务收到的现金': 'cashFromGoodsSalesAndServicesProvided',
    '收到的税费返还': 'refundOfTaxAndFeeReceived',
    '收到其他与经营活动有关的现金': 'otherCashRelatedBusinessActivitiesReceived',
    '经营活动现金流入小计': 'cashInflowsFromOperatingActivities',
    '购买商品、接受劳务支付的现金': 'buyingGoodsReceivingCashPaidForLabor',
    '支付给职工以及为职工支付的现金': 'paymentToEmployeesAndCashPaidForEmployees',
    '支付的各项税费': 'paymentsOfVariousTaxes',
    '支付其他与经营活动有关的现金': 'paymentOfOtherCashRelatedToBusinessActivities',
    '经营活动现金流出小计': 'cashOutflowsFromOperatingActivities',
    '经营活动产生的现金流量净额': 'netCashFlowsFromOperatingActivities',
    ### 投资活动 Investment
    '收回投资收到的现金': 'cashReceivedFromInvestmentReceived',
    '取得投资收益收到的现金': 'cashReceivedFromInvestmentIncome',
    '处置固定资产、无形资产和其他长期资产收回的现金净额': 'disposalOfNetCashForRecoveryOfFixedAssetsIntangibleAssetsAndOtherLongTermAssets',
    '处置子公司及其他营业单位收到的现金净额': 'disposalOfNetCashReceivedFromSubsidiariesAndOtherBusinessUnits',
    '收到其他与投资活动有关的现金': 'otherCashReceivedRelatingToInvestingActivities',
    '投资活动现金流入小计': 'cashinFlowsFromInvestmentActivities',
    '购建固定资产、无形资产和其他长期资产支付的现金': 'cashForThePurchaseConstructionPaymentOfFixedAssetsIntangibleAssetsAndOtherLongTermAssets',
    '投资支付的现金': 'cashInvestment',
    '取得子公司及其他营业单位支付的现金净额': 'acquisitionOfNetCashPaidBySubsidiariesAndOtherBusinessUnits',
    '支付其他与投资活动有关的现金': 'otherCashPaidRelatingToInvestingActivities',
    '投资活动现金流出小计': 'cashOutflowsFromInvestmentActivities',
    '投资活动产生的现金流量净额':'netCashFlowsFromInvestingActivities',
    ### 筹资活动 Financing
    '吸收投资收到的现金':'cashReceivedFromInvestors',
    '取得借款收到的现金':'cashFromBorrowings',
    '收到其他与筹资活动有关的现金':'otherCashReceivedRelatingToFinancingActivities',
    '筹资活动现金流入小计':'cashInflowsFromFinancingActivities',
    '偿还债务支付的现金':'cashPaymentsOfAmountBorrowed',
    '分配股利、利润或偿付利息支付的现金':'cashPaymentsForDistrbutionOfDividendsOrProfits',
    '支付其他与筹资活动有关的现金':'otherCashPaymentRelatingToFinancingActivities',
    '筹资活动现金流出小计':'cashOutflowsFromFinancingActivities',
    '筹资活动产生的现金流量净额':'netCashFlowsFromFinancingActivities',
    ### 汇率变动
    '四、汇率变动对现金的影响':'effectOfForeignExchangRateChangesOnCash',
    '四(2)、其他原因对现金的影响':'effectOfOtherReasonOnCash',
    ### 现金及现金等价物净增加
    '五、现金及现金等价物净增加额':'netIncreaseInCashAndCashEquivalents',
    '期初现金及现金等价物余额':'initialCashAndCashEquivalentsBalance',
    ### 期末现金及现金等价物余额
    '期末现金及现金等价物余额':'theFinalCashAndCashEquivalentsBalance',
    '净利润':'',
    '加：资产减值准备':'',
    '固定资产折旧、油气资产折耗、生产性生物资产折旧':'',
    '无形资产摊销':'',
    '长期待摊费用摊销':'',
    '处置固定资产、无形资产和其他长期资产的损失':'',
    '固定资产报废损失':'',
    '公允价值变动损失':'',
    '财务费用':'',
    '投资损失':'',
    '递延所得税资产减少':'',
    '递延所得税负债增加':'',
    '存货的减少':'',
    '经营性应收项目的减少':'',
    '经营性应付项目的增加':'',
    '其他':'',
    '经营活动产生的现金流量净额2':'',
    '债务转为资本':'',
    '一年内到期的可转换公司债券':'',
    '融资租入固定资产':'',
    '现金的期末余额':'',
    '减：现金的期初余额':'',
    '加：现金等价物的期末余额':'',
    '减：现金等价物的期初余额':'',
    '现金及现金等价物净增加额':'',
    ## 偿债能力分析
    '流动比率':'',
    '速动比率':'',
    '现金比率(%)':'',
    '利息保障倍数':'',
    '非流动负债比率(%)':'',
    '流动负债比率(%)':'',
    '现金到期债务比率(%)':'',
    '有形资产净值债务率(%)':'',
    '权益乘数(%)':'',
    '股东的权益/负债合计(%)':'',
    '有形资产/负债合计(%)':'',
    '经营活动产生的现金流量净额/负债合计(%)':'',
    'EBITDA/负债合计(%)':'',
    ## 经营效率分析
    '应收帐款周转率':'',
    '存货周转率':'',
    '运营资金周转率':'',
    '总资产周转率':'',
    '固定资产周转率':'',
    '应收帐款周转天数':'',
    '存货周转天数':'',
    '流动资产周转率':'',
    '流动资产周转天数':'',
    '总资产周转天数':'',
    '股东权益周转率':'',
    '营业收入增长率(%)':'',
    ## 发展能力分析
    '净利润增长率(%)':'',
    '净资产增长率(%)':'',
    '固定资产增长率(%)':'',
    '总资产增长率(%)':'',
    '投资收益增长率(%)':'',
    '营业利润增长率(%)':'',
    '暂无':'',
    '暂无':'',
    '暂无':'',
    ## 获利能力分析
    '成本费用利润率(%)':'',
    '营业利润率':'',
    '营业税金率':'',
    '营业成本率':'',
    '净资产收益率':'',
    '投资收益率':'',
    '销售净利率(%)':'',
    '总资产报酬率':'',
    '净利润率':'',
    '销售毛利率(%)':'',
    '三费比重':'',
    '管理费用率':'',
    '财务费用率':'',
    '扣除非经常性损益后的净利润':'',
    '息税前利润(EBIT)':'',
    '息税折旧摊销前利润(EBITDA)':'',
    'EBITDA/营业总收入(%)':''
    ## 资本结构分析
}
