import pandas as pd
import json
import requests
import time
class xms_quant_trader_data:
    '''
    索普金融量化交易数据库2
    作者:索普量化
    微信:xms_quant
    '''
    def __init__(self,
            url='http://14.103.193.242',
            port='8080',
            password='test'):
        print('''
        索普金融量化交易数据库3
        作者:索普量化
        微信:xms_quant
        教程网页:https://gitcode.com/qq_50882340/xms_quant_trader_data
        账号管理网页:http://14.103.193.242:8088/
        量化学习网页:http://14.103.193.242:9999/xms_quants.html
        获取的授权码找我申请
        ''')
        print('服务器{} 端口{} 授权码{}'.format(url,port,password))
        self.url=url
        self.port=port
        self.password=password
        print(self.get_user_info())
    def get_user_info(self):
        '''
        获取使用者信息
        '''
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_info')
        params={
           'password':self.password
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        return res
    def check_password_is_av_user(self):
        '''
        检查授权码是否可以使用
        '''
        url='{}:{}/{}?'.format(self.url,self.port,'check_password_is_av_user')
        params={
           'password':self.password
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        return res

    def get_full_tick(self,stock='513100.SH'):
        '''
        获取tick数据
        'time'                  #时间戳
        'lastPrice'             #最新价
        'open'                  #开盘价
        'high'                  #最高价
        'low'                   #最低价
        'lastClose'             #前收盘价
        'amount'                #成交总额
        'volume'                #成交总量
        'pvolume'               #原始成交总量
        'stockStatus'           #证券状态
        'openInt'               #持仓量
        'lastSettlementPrice'   #前结算
        'askPrice'              #委卖价
        'bidPrice'              #委买价
        'askVol'                #委卖量
        'bidVol'                #委买量
        'transactionNum'		#成交笔数
        '''
        url='{}:{}/{}?'.format(self.url,self.port,'get_full_tick')
        params={
            'password':self.password,
            'stock':stock
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        return res
    def get_full_all_tick(self,code_list=['513100.SH','600031.SH']):
        '''
        获取多个标的tick数据
        http://127.0.0.1:5000/get_full_all_tick?code_list=513100.SH,600031.SH
        'time'                  #时间戳
        'lastPrice'             #最新价
        'open'                  #开盘价
        'high'                  #最高价
        'low'                   #最低价
        'lastClose'             #前收盘价
        'amount'                #成交总额
        'volume'                #成交总量
        'pvolume'               #原始成交总量
        'stockStatus'           #证券状态
        'openInt'               #持仓量
        'lastSettlementPrice'   #前结算
        'askPrice'              #委卖价
        'bidPrice'              #委买价
        'askVol'                #委卖量
        'bidVol'                #委买量
        'transactionNum'		#成交笔数
        '''
        url='{}:{}/{}?'.format(self.url,self.port,'get_full_all_tick')
        params={
            'password':self.password,
            'code_list':','.join(code_list)
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        return res
    def get_market_data_ex(self,
            stock_code='513100.SH', 
            period='1d', 
            start_time='20250101', 
            end_time='20500101', 
            count=-1):
        '''
        获取历史行情数据
        :param field_list: 行情数据字段列表，[]为全部字段
            K线可选字段：
                "time"                #时间戳
                "open"                #开盘价
                "high"                #最高价
                "low"                 #最低价
                "close"               #收盘价
                "volume"              #成交量
                "amount"              #成交额
                "settle"              #今结算
                "openInterest"        #持仓量
            分笔可选字段：
                "time"                #时间戳
                "lastPrice"           #最新价
                "open"                #开盘价
                "high"                #最高价
                "low"                 #最低价
                "lastClose"           #前收盘价
                "amount"              #成交总额
                "volume"              #成交总量
                "pvolume"             #原始成交总量
                "stockStatus"         #证券状态
                "openInt"             #持仓量
                "lastSettlementPrice" #前结算
                "askPrice1", "askPrice2", "askPrice3", "askPrice4", "askPrice5" #卖一价~卖五价
                "bidPrice1", "bidPrice2", "bidPrice3", "bidPrice4", "bidPrice5" #买一价~买五价
                "askVol1", "askVol2", "askVol3", "askVol4", "askVol5"           #卖一量~卖五量
                "bidVol1", "bidVol2", "bidVol3", "bidVol4", "bidVol5"           #买一量~买五量
        :param stock_list: 证券代码 "000001.SZ"
        :param period: 周期 分笔"tick" 分钟线"1m"/"5m" 日线"1d"
        :param start_time: 起始时间 "20200101" "20200101093000"
        :param end_time: 结束时间 "20201231" "20201231150000"
        :param count: 数量 -1全部/n: 从结束时间向前数n个
        :param dividend_type: 除权类型"none" "front" "back" "front_ratio" "back_ratio"
        :param fill_data: 对齐时间戳时是否填充数据，仅对K线有效，分笔周期不对齐时间戳
            为True时，以缺失数据的前一条数据填充
                open、high、low、close 为前一条数据的close
                amount、volume为0
                settle、openInterest 和前一条数据相同
            为False时，缺失数据所有字段填NaN
        :return: 数据集，分笔数据和K线数据格式不同
            period为'tick'时：{stock1 : value1, stock2 : value2, ...}
                stock1, stock2, ... : 合约代码
                value1, value2, ... : np.ndarray 数据列表，按time增序排列
            period为其他K线周期时：{field1 : value1, field2 : value2, ...}
                field1, field2, ... : 数据字段
                value1, value2, ... : pd.DataFrame 字段对应的数据，各字段维度相同，index为stock_list，columns为time_list
        
        '''
        url='{}:{}/{}?'.format(self.url,self.port,'get_market_data_ex')
        params={
            'password':self.password,
            'stock_code':stock_code, 
            'period':period, 
            'start_time':start_time, 
            'end_time':end_time, 
            
            
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        return res
    def data_to_pandas(self,data):
        try:
            df=pd.DataFrame(data)
        except:
            df=pd.DataFrame()
            for keys,value in data.items():
                df[keys]=[value]
                
        return df
    def get_wencai_data(self,
        query='今日涨停',
        ):
        '''
        获取问财数据
        '''
        url='{}:{}/{}?'.format(self.url,self.port,'get_wencai_data')
        params={
            'password':self.password,
            'query':query
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        return res
    def get_user_def_data(self,
        name='df',
        func= """
        import akshare as ak
        df = ak.stock_zt_pool_em(date='20250711')
        """):
        '''
        获取自定义函数数据
        '''
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_def_data')
        params={
            'password':self.password,
            'name':name,
            "func":func
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        return res
    
    def get_bond_cov_spot_data(self,
            url='http://124.220.32.224',
            port='8023',
            date='20250711'):
        '''
        获取可转债实时数据
        '''
        func='''
        import requests
        import pandas as pd
        try:
            url='{}:{}/data/实时数据/{}.json?t=1752251108452'
            res=requests.get(url=url)
            res=res.json()
            df=pd.DataFrame(res)
        except Exception as e:
            print(e,'获取实时数据表有问题')
            df=pd.DataFrame()
        '''.format(url,port,date)
        df=self.get_user_def_data(func=func)
        return df
    def get_bond_cov_all_mr_factor_data(self,
            url='http://124.220.32.224',
            port='8023',
            date='20250711'):
        '''
        获取可转债全部默认因子数据
        '''
        func='''
        import requests
        import pandas as pd
        try:
            url='{}:{}/data/全部默认因子/{}.json?t=1752251108452'
            res=requests.get(url=url)
            res=res.json()
            df=pd.DataFrame(res)
        except Exception as e:
            print(e,'获取全部默认因子表有问题')
            df=pd.DataFrame()
        '''.format(url,port,date)
        df=self.get_user_def_data(func=func)
        return df
    def get_bond_cov_all_connect_factor_data(self,
            url='http://124.220.32.224',
            port='8023',
            date='20250711'):
        '''
        获取可转债合成因子因子数据
        '''
        func='''
        import requests
        import pandas as pd
        try:
            url='{}:{}/data/合成因子/{}.json?t=1752251108452'
            res=requests.get(url=url)
            res=res.json()
            df=pd.DataFrame(res)
        except Exception as e:
            print(e,'获取全部默认因子表有问题')
            df=pd.DataFrame()
        '''.format(url,port,date)
        df=self.get_user_def_data(func=func)
        return df
    def get_instrument_detail(self,stock='600031.SH'):
        '''
        获取可标的的基础数据
        ExchangeID - string 合约市场代码
        InstrumentID - string 合约代码
        InstrumentName - string 合约名称
        ProductID - string 合约的品种ID(期货)
        ProductName - string 合约的品种名称(期货)
        ExchangeCode - string 交易所代码
        UniCode - string 统一规则代码
        CreateDate - str 上市日期(期货)
        OpenDate - str IPO日期(股票)
        ExpireDate - int 退市日或者到期日
        PreClose - float 前收盘价格
        SettlementPrice - float 前结算价格
        UpStopPrice - float 当日涨停价
        DownStopPrice - float 当日跌停价
        FloatVolume - float 流通股本
        TotalVolume - float 总股本
        LongMarginRatio - float 多头保证金率
        ShortMarginRatio - float 空头保证金率
        PriceTick - float 最小价格变动单位
        VolumeMultiple - int 合约乘数(对期货以外的品种，默认是1)
        MainContract - int 主力合约标记，1、2、3分别表示第一主力合约，第二主力合约，第三主力合约
        LastVolume - int 昨日持仓量
        InstrumentStatus - int 合约停牌状态
        IsTrading - bool 合约是否可交易
        IsRecent - bool 是否是近月合约
        OpenInterestMultiple - int 交割月持仓倍数 

        '''
        url='{}:{}/{}?'.format(self.url,self.port,'get_instrument_detail')
        params={
            'password':self.password,
            'stock':stock
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        return res
    def get_all_maker_stock(self):
        '''
        获取全市场股票
        '''
        file_path: str = '/data/全市场股票/'
        file_name: str = '全市场股票'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def adjust_stock_1(self,x=''):
        return '0'*(6-len(str(x)))+str(x)
    def adjust_stock(stock='600031.SH'):
        '''
        调整代码
        '''
        if stock[-2:]=='SH' or stock[-2:]=='SZ' or stock[-2:]=='sh' or stock[-2:]=='sz':
            stock=stock.upper()
        else:
            if stock[:3] in ['600','601','603','605','688','689',
                ] or stock[:2] in ['11','51','58'] or stock[:1] in ['5']:
                stock=stock+'.SH'
            else:
                stock=stock+'.SZ'
        return stock
    def get_stock_daily_hist_data(self,stock='301088',start_date='20200101',end_date='20500101'):
        '''
        获取股票日线行情数据
        '''
        file_path: str = '/data/股票日线行情/'
        file_name: str = '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        
        return df
    def get_maker_all_ETF(self):
        '''
        获取市场全部ETF
        '''
        file_path= '/data/{}/'.format('市场全部ETF')
        file_name= '{}'.format('市场全部ETF')
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_ETF_daily_hist_data(self,stock='512890',start_date='20200101',end_date='20500101'):
        '''
        获取ETF日线行情数据
        '''
        file_path: str = '/data/ETF日线行情/'
        file_name: str = '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        
        return df
    def get_maker_bond_cov_data(self):
        '''
        获取全市场可转债
        '''
        file_path= '/data/{}/'.format('全部可转债')
        file_name= '{}'.format('全部可转债')
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_bond_cov_daily_hist_data(self,stock='113575',start_date='20200101',end_date='20500101'):
        '''
        获取可转债日线行情数据
        '''
        file_path: str = '/data/可转债日线行情/'
        file_name: str = '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        
        return df
    
    #同花顺涨停
    def get_ths_zt_data(self,date='20250910'):
        '''
        同花顺涨停数据
        '''
        name='同花顺涨停数据'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    
    def get_ths_cczt_data(self,date='20250910'):
        '''
        同花顺冲刺涨停数据
        '''
        name='同花顺冲刺涨停数据'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_ths_dt_data(self,date='20250910'):
        '''
        同花顺跌停数据
        '''
        name='同花顺跌停数据'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    
    def get_ths_lbtt_data(self,date='20250910'):
        '''
        同花顺连扳天梯数据
        '''
        name='同花顺连扳天梯数据'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_ths_zbc_data(self,date='20250910'):
        '''
        同花顺炸板数据
        '''
        name='同花顺炸板数据'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    #同花顺人气排行
    def get_ths_stock_hot_rank(self,date='20250910'):
        '''
        同花顺股票人气排行
        '''
        name='同花顺股票人气排行'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_ths_etf_hot_rank(self,date='20250910'):
        '''
        同花顺基金人气排行
        '''
        name='同花顺基金人气排行'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_ths_concept_hot_rank(self,date='20250910'):
        '''
        同花顺概念人气排行
        '''
        name='同花顺概念人气排行'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_ths_industry_hot_rank(self,date='20250910'):
        '''
        同花顺行业人气排行
        '''
        name='同花顺行业人气排行'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_ths_bond_hot_rank(self,date='20250910'):
        '''
        同花顺可转债人气排行
        '''
        name='同花顺可转债人气排行'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_ths_hk_hot_rank(self,date='20250910'):
        '''
        同花顺港股人气排行
        '''
        name='同花顺港股人气排行'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_ths_us_hot_rank(self,date='20250910'):
        '''
        同花顺美股人气排行
        '''
        name='同花顺美股人气排行'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    #行业数据
    def stock_board_industry_summary_ths(self):
        '''
        同花顺行业一览表
        输出参数
        名称	类型	描述
        序号	int64	-
        板块	object	-
        涨跌幅	object	注意单位: %
        总成交量	float64	注意单位: 万手
        总成交额	float64	注意单位: 亿元
        净流入	float64	注意单位: 亿元
        上涨家数	float64	-
        下跌家数	float64	-
        均价	float64	-
        领涨股	float64	-
        领涨股-最新价	object	-
        领涨股-涨跌幅	object	注意单位: %

        '''
        name='同花顺行业一览表'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_board_industry_summary_ths_2(self):
        '''
        同花顺全部行业
        输出参数
        名称	类型	描述
        序号	int64	-
        板块	object	-
        涨跌幅	object	注意单位: %
        总成交量	float64	注意单位: 万手
        总成交额	float64	注意单位: 亿元
        净流入	float64	注意单位: 亿元
        上涨家数	float64	-
        下跌家数	float64	-
        均价	float64	-
        领涨股	float64	-
        领涨股-最新价	object	-
        领涨股-涨跌幅	object	注意单位: %

        '''
        name='同花顺全部行业'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    
    def get_ths_industry_stock(self,stock='881143'):
        '''
        同花顺行业成分股
        '''
        name='同花顺行业成分股'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df

    
    def stock_board_industry_index_ths(self,
                stock='半导体',
                start_date='20250101',
                end_date='20500101'):
        '''
        同花顺行业指数行情数据
        '''
        name='同花顺行业指数行情数据'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        df['日期']=pd.to_datetime(df['日期'])
        df=df[df['日期']>=start_date]
        df=df[df['日期']<=end_date]
        return df
    def stock_board_industry_name_em(self):
        '''
        东方财富行业板块
        名称	类型	描述
        排名	int64	-
        板块名称	object	-
        板块代码	object	-
        最新价	float64	-
        涨跌额	float64	-
        涨跌幅	float64	注意单位：%
        总市值	int64	-
        换手率	float64	注意单位：%
        上涨家数	int64	-
        下跌家数	int64	-
        领涨股票	object	-
        领涨股票-涨跌幅	float64	注意单位：%
        '''
        name='东方财富行业板块'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_board_industry_hist_em(self,
                stock='半导体',
                start_date='20250101',
                end_date='20500101'):
        '''
        东方财富行业板块历史行情数据
        '''
        name='东方财富行业板块历史行情数据'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        df['日期']=pd.to_datetime(df['日期'])
        df=df[df['日期']>=start_date]
        df=df[df['日期']<=end_date]
        return df
    def stock_board_industry_cons_em(self,stock='半导体'):
        '''
        东方财富行业成份股
        '''
        name='东方财富行业成份股'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    #东方财富涨停数据
    def stock_zt_pool_em(self,date='20250912'):
        '''
        东方财富涨停股池
        '''
        name='东方财富涨停股池'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_zt_pool_previous_em(self,date='20250912'):
        '''
        东方财富涨停股池
        '''
        name='东方财富昨日涨停股'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_zt_pool_strong_em(self,date='20250912'):
        '''
        东方财富强势股池
        '''
        name='东方财富强势股池'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_zt_pool_sub_new_em(self,date='20250912'):
        '''
        东方财富次新股池
        '''
        name='东方财富次新股池'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_zt_pool_zbgc_em(self,date='20250912'):
        '''
        东方财富炸板股池
        '''
        name='东方财富炸板股池'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_zt_pool_dtgc_em(self,date='20250912'):
        '''
        东方财富跌停股票池
        '''
        name='东方财富跌停股票池'
        file_path= '/data/{}/'.format(name)
        file_name= '{}_{}'.format(date,name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    #概念数据
    def stock_board_concept_name_ths(self):
        '''
        同花顺全部概念
        '''
        name='同花顺全部概念'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    
    def stock_board_concept_info(self):
        '''
        同花顺全部概念详情
        '''
        name='同花顺全部概念详情'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    
    def get_ths_concept_stock(self,stock='886105'):
        '''
        同花顺概念成分股
        '''
        name='同花顺概念成分股'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df


    def stock_board_concept_index_ths(self,stock='AI手机'):
        '''
        同花顺概念板块日线指数
        '''
        name='同花顺概念板块日线指数'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_board_concept_name_em(self):
        '''
        东方财富全部概念板块
        '''
        name='东方财富全部概念板块'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_board_concept_cons_em(self,stock='白酒'):
        '''
        东方财富概念成份股
        '''
        name='东方财富概念成份股'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_board_concept_hist_em(self,stock='白酒'):
        '''
        东方财富概念历史行情数据
        '''
        name='东方财富概念历史行情数据'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    #资金流数据
    def stock_fund_flow_individual(self,date='20250909',symbol='3日排行'):
        '''
        同花顺个股资金流
        symbol="即时"; choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"}
        输出结果
        名称	类型	描述
        序号	int32	-
        股票代码	int64	-
        股票简称	object	-
        最新价	float64	-
        阶段涨跌幅	object	注意单位: %
        连续换手率	object	注意单位: %
        资金流入净额	float64	注意单位: 元

        '''
        file_path= '/data/同花顺个股资金流/'
        file_name= '{}_{}'.format(date,symbol)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_fund_flow_concept(self,date='20250909',symbol='3日排行'):
        '''
        同花顺概念资金流
        输出参数-3日、5日、10日和20日
        名称	类型	描述
        序号	int32	-
        行业	object	-
        公司家数	int64	-
        行业指数	float64	-
        阶段涨跌幅	object	注意单位: %
        流入资金	float64	注意单位: 亿
        流出资金	float64	注意单位: 亿
        净额	float64	注意单位: 亿
        '''
        file_path= '/data/同花顺概念资金流/'
        file_name= '{}_{}'.format(date,symbol)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_fund_flow_industry(self,date='20250909',symbol='3日排行'):
        '''
        同花顺行业资金流
        输出参数-3日、5日、10日和20日

        名称	类型	描述
        序号	int32	-
        行业	object	-
        公司家数	int64	-
        行业指数	float64	-
        阶段涨跌幅	object	注意单位: %
        流入资金	float64	注意单位: 亿
        流出资金	float64	注意单位: 亿
        净额	float64	注意单位: 亿

        '''
        file_path= '/data/同花顺行业资金流/'
        file_name= '{}_{}'.format(date,symbol)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_individual_fund_flow_rank(self,date='20250909',indicator='3日'):
        '''
        东方财富个股资金流排名
        indicator="今日"; choice {"今日", "3日", "5日", "10日"}
        名称	类型	描述
        序号	int64	-
        代码	object	-
        名称	object	-
        最新价	float64	-
        今日涨跌幅	float64	注意单位: %
        今日主力净流入-净额	float64	-
        今日主力净流入-净占比	float64	注意单位: %
        今日超大单净流入-净额	float64	-
        今日超大单净流入-净占比	float64	注意单位: %
        今日大单净流入-净额	float64	-
        今日大单净流入-净占比	float64	注意单位: %
        今日中单净流入-净额	float64	-
        今日中单净流入-净占比	float64	注意单位: %
        今日小单净流入-净额	float64	-
        今日小单净流入-净占比	float64	注意单位: %
        '''
        file_path= '/data/东方财富个股资金流排名/'
        file_name= '{}_{}'.format(date,indicator)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_sector_fund_flow_rank(self,
                date='20250909',
                indicator='今日',
                sector_type='行业资金流'
                ):
        '''
        东方财富板块资金流排名
        indicator	str	indicator="今日"; choice of {"今日", "5日", "10日"}
        sector_type	str	sector_type="行业资金流"; choice of {"行业资金流", "概念资金流", "地域资金流"}
        
        名称	类型	描述
        序号	int64	-
        名称	object	-
        今日涨跌幅	float64	注意单位: %
        主力净流入-净额	float64	-
        主力净流入-净占比	float64	注意单位: %
        超大单净流入-净额	float64	-
        超大单净流入-净占比	float64	注意单位: %
        大单净流入-净额	float64	-
        大单净流入-净占比	float64	注意单位: %
        中单净流入-净额	float64	-
        中单净流入-净占比	float64	注意单位: %
        小单净流入-净额	float64	-
        小单净流入-净占比	float64	注意单位: %
        主力净流入最大股	object	-

        '''
        file_path= '/data/东方财富板块资金流排名/'
        file_name= '{}_{}_{}'.format(date,indicator,sector_type)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_main_fund_flow(self,date='20250909',symbol='全部股票'):
        '''
        东方财富主力净流入排名
        symbol	str	symbol="全部股票"；choice of {"全部股票", "沪深A股", "沪市A股", "科创板", "深市A股", "创业板", "沪市B股", "深市B股"}
        输出参数
        名称	类型	描述
        序号	int64	-
        代码	object	-
        名称	object	-
        最新价	float64	-
        今日排行榜-主力净占比	float64	注意单位: %
        今日排行榜-今日排名	float64	-
        今日排行榜-今日涨跌	float64	注意单位: %
        5日排行榜-主力净占比	float64	注意单位: %
        5日排行榜-5日排名	int64	-
        5日排行榜-5日涨跌	float64	注意单位: %
        10日排行榜-主力净占比	float64	注意单位: %
        10日排行榜-10日排名	int64	-
        10日排行榜-10日涨跌	float64	注意单位: %
        所属板块	object	-
        '''
        file_path= '/data/东方财富主力净流入排名/'
        file_name= '{}_{}'.format(date,symbol)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_stock_maker(self,stock='600031.SH'):
        '''
        获取股票市场
        '''
        if stock[:3] in ['600','601','603','605','688','689',
            ] or stock[:2] in ['11','51','58'] or stock[:1] in ['5']:
            stock='sh'
        else:
            stock='sz'
        return stock
    #*****************************
    def stock_individual_fund_flow(self,stock='600031'):
        '''
        东方财富个股资金流
        名称	类型	描述
        日期	object	-
        收盘价	float64	-
        涨跌幅	float64	注意单位: %
        主力净流入-净额	float64	-
        主力净流入-净占比	float64	注意单位: %
        超大单净流入-净额	float64	-
        超大单净流入-净占比	float64	注意单位: %
        大单净流入-净额	float64	-
        大单净流入-净占比	float64	注意单位: %
        中单净流入-净额	float64	-
        中单净流入-净占比	float64	注意单位: %
        小单净流入-净额	float64	-
        小单净流入-净占比	float64	注意单位: %
        '''
        file_path= '/data/东方财富个股资金流/'
        file_name= '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_market_fund_flow(self):
        '''
        东方财富大盘资金流
        输出参数
        名称	类型	描述
        日期	object	-
        上证-收盘价	float64	-
        上证-涨跌幅	float64	注意单位: %
        深证-收盘价	float64	-
        深证-涨跌幅	float64	注意单位: %
        主力净流入-净额	float64	-
        主力净流入-净占比	float64	注意单位: %
        超大单净流入-净额	float64	-
        超大单净流入-净占比	float64	注意单位: %
        大单净流入-净额	float64	-
        大单净流入-净占比	float64	注意单位: %
        中单净流入-净额	float64	-
        中单净流入-净占比	float64	注意单位: %
        小单净流入-净额	float64	-
        小单净流入-净占比	float64	注意单位: %
        '''
        name='东方财富大盘资金流'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_sector_fund_flow_hist(self,symbol='半导体'):
        '''
        东方财富行业历史资金流
        名称	类型	描述
        日期	object	注意单位: %
        主力净流入-净额	float64	-
        主力净流入-净占比	float64	注意单位: %
        超大单净流入-净额	float64	-
        超大单净流入-净占比	float64	注意单位: %
        大单净流入-净额	float64	-
        大单净流入-净占比	float64	注意单位: %
        中单净流入-净额	float64	-
        中单净流入-净占比	float64	注意单位: %
        小单净流入-净额	float64	-
        小单净流入-净占比	float64	注意单位: %
        '''
        name='东方财富行业历史资金流'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(symbol)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_concept_fund_flow_hist(self,symbol='数据要素'):
        '''
        东方财富概念历史资金流
        输出参数
        名称	类型	描述
        日期	object	注意单位: %
        主力净流入-净额	float64	-
        主力净流入-净占比	float64	注意单位: %
        超大单净流入-净额	float64	-
        超大单净流入-净占比	float64	注意单位: %
        大单净流入-净额	float64	-
        大单净流入-净占比	float64	注意单位: %
        中单净流入-净额	float64	-
        中单净流入-净占比	float64	注意单位: %
        小单净流入-净额	float64	-
        小单净流入-净占比	float64	注意单位: %
        '''
        name='东方财富概念历史资金流'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(symbol)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_cyq_em(self,stock='600031'):
        '''
        东方财富筹码分布
        '''
        name='东方财富筹码分布'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_yjbb_em(self,date='20250930'):
        '''
        业绩报表
        输出参数
        名称	类型	描述
        序号	int64	-
        股票代码	object	-
        股票简称	object	-
        每股收益	float64	注意单位: 元
        营业总收入-营业总收入	float64	注意单位: 元
        营业总收入-同比增长	float64	注意单位: %
        营业总收入-季度环比增长	float64	注意单位: %
        净利润-净利润	float64	注意单位: 元
        净利润-同比增长	float64	注意单位: %
        净利润-季度环比增长	float64	注意单位: %
        每股净资产	float64	注意单位: 元
        净资产收益率	float64	注意单位: %
        每股经营现金流量	float64	注意单位: 元
        销售毛利率	float64	注意单位: %
        所处行业	object	-
        最新公告日期	object	-
        '''
        name='业绩报表'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_yjkb_em(self,date='20250930'):
        '''
        业绩快报
        输出参数
        名称	类型	描述
        序号	object	-
        股票代码	object	-
        股票简称	object	-
        每股收益	object	-
        营业收入-营业收入	object	-
        营业收入-去年同期	object	-
        营业收入-同比增长	str	-
        营业收入-季度环比增长	object	-
        净利润-净利润	object	-
        净利润-去年同期	object	-
        净利润-同比增长	str	-
        净利润-季度环比增长	object	-
        每股净资产	object	-
        净资产收益率	object	-
        所处行业	object	-
        公告日期	object	-
        市场板块	object	-
        证券类型	object	-
        '''
        name='业绩快报'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_zcfz_em(self,date='20250930'):
        '''
        资产负债表
        输出参数
        名称	类型	描述
        序号	int64	-
        股票代码	object	-
        股票简称	object	-
        资产-货币资金	float64	注意单位: 元
        资产-应收账款	float64	注意单位: 元
        资产-存货	float64	注意单位: 元
        资产-总资产	float64	注意单位: 元
        资产-总资产同比	float64	注意单位: %
        负债-应付账款	float64	注意单位: 元
        负债-总负债	float64	注意单位: 元
        负债-预收账款	float64	注意单位: 元
        负债-总负债同比	float64	注意单位: %
        资产负债率	float64	注意单位: %
        股东权益合计	float64	注意单位: 元
        公告日期	object	-
        '''
        name='资产负债表'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_lrb_em(self,date='20250930'):
        '''
        利润表
        输出参数
        名称	类型	描述
        序号	int64	-
        股票代码	object	-
        股票简称	object	-
        净利润	float64	注意单位: 元
        净利润同比	float64	注意单位: %
        营业总收入	float64	注意单位: 元
        营业总收入同比	float64	注意单位: %
        营业总支出-营业支出	float64	注意单位: 元
        营业总支出-销售费用	float64	注意单位: 元
        营业总支出-管理费用	float64	注意单位: 元
        营业总支出-财务费用	float64	注意单位: 元
        营业总支出-营业总支出	float64	注意单位: 元
        营业利润	float64	注意单位: 元
        利润总额	float64	注意单位: 元
        公告日期	object	-
        '''
        name='利润表'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_xjll_em(self,date='20250930'):
        '''
        现金流量表
        '''
        name='现金流量表'
        file_path= '/data/{}/'.format(name)
        file_name= '{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def conv_time(self,ct):
        '''
        conv_time(1476374400000) --> '20161014000000.000'
        '''
        local_time = time.localtime(ct / 1000)
        data_head = time.strftime('%Y%m%d%H%M%S', local_time)
        data_secs = (ct - int(ct)) * 1000
        time_stamp = '%s.%03d' % (data_head, data_secs)
        return time_stamp
    #*****************************************
    #00000000
    def fund_etf_spot_em(self):
        '''
        ETF基金实时行情东财
        '''
        name='ETF基金实时行情东财'
        file_path= '/data/{}/'.format(name)
        file_name='ETF基金实时行情东财'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def fund_etf_spot_ths(self):
        '''
        ETF基金实时行情同花顺
        '''
        name='ETF基金实时行情同花顺'
        file_path= '/data/{}/'.format(name)
        file_name='ETF基金实时行情同花顺'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def fund_etf_hist_em(self,stock='159869',start_date='20210101',end_date='20500101'):
        '''
        ETF基金历史行情
        '''
        name='ETF基金历史行情'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        df=df[df['日期']>=start_date]
        df=df[df['日期']<=end_date]
        return df
    #可转债数据
    
    def bond_zh_cov(self):
        '''
        可转债数据一览表
        '''
        name='可转债数据一览表'
        file_path= '/data/{}/'.format(name)
        file_name='可转债数据一览表'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def bond_zh_cov_value_analysis(self):
        '''
        可转债价值分析
        '''
        name='可转债价值分析'
        file_path= '/data/{}/'.format(name)
        file_name='可转债价值分析'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def bond_cb_redeem_jsl(self):
        '''
        可转债强赎
        '''
        name='可转债强赎'
        file_path= '/data/{}/'.format(name)
        file_name='可转债强赎'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def bond_cb_index_jsl(self):
        '''
        集思录可转债等权指数
        '''
        name='集思录可转债等权指数'
        file_path= '/data/{}/'.format(name)
        file_name='集思录可转债等权指数'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def bond_zh_hs_daily(self,stock='sz123241',start_date='20200101',end_date='20500101'):
        '''
        可转债历史数据
        '''
        name='可转债历史数据'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        df=df[df['date']>=start_date]
        df=df[df['date']<=end_date]
        return df
    
    def stock_zh_a_daily(self,stock='sz000001',start_date='20200101',end_date='20500101'):
        '''
        历史行情数据新浪
        '''
        name='历史行情数据新浪'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        df=df[df['date']>=start_date]
        df=df[df['date']<=end_date]
        return df
    
    def stock_zh_index_spot_sina(self):
        '''
        指数实时行情数据
        '''
        name='指数实时行情数据'
        file_path= '/data/{}/'.format(name)
        file_name='指数实时行情数据'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_zh_index_daily(self,stock='sh000001',start_date='20200101',end_date='20500101'):
        '''
        指数历史行情数据
        '''
        name='指数历史行情数据'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        df=df[df['date']>=start_date]
        df=df[df['date']<=end_date]
        return df
    def index_stock_cons(self,stock='sh000001'):
        '''
        股票指数成份
        '''
        name='股票指数成份'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    
    def index_all_cni(self):
        '''
        国证指数
        '''
        name='国证指数'
        file_path= '/data/{}/'.format(name)
        file_name='国证指数'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    
    def index_detail_cni(self,stock='399001'):
        '''
        国证指数成份股
        '''
        name='国证指数成份股'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    
    def index_hist_cni(self,stock='399001',start_date='20200101',end_date='20500101'):
        '''
        国证指数历史行情
        '''
        name='国证指数历史行情'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        df=df[df['日期']>=start_date]
        df=df[df['日期']<=end_date]
        return df
    
    def sw_index_first_info(self):
        '''
        申万一级行业信息
        '''
        name='申万一级行业信息'
        file_path= '/data/{}/'.format(name)
        file_name='申万一级行业信息'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def sw_index_second_info(self):
        '''
        申万二级行业信息
        '''
        name='申万二级行业信息'
        file_path= '/data/{}/'.format(name)
        file_name='申万二级行业信息'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def sw_index_third_info(self):
        '''
        申万三级行业信息
        '''
        name='申万三级行业信息'
        file_path= '/data/{}/'.format(name)
        file_name='申万三级行业信息'
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df

    def sw_index_third_cons(self,stock='850111.SI'):
        '''
        申万三级行业成份股
        '''
        name='申万三级行业成份股'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(stock)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    #ptrade财务数据
    def get_valuation(self,date='20250930'):
        '''
        估值数据
        date没有输入返回全部数据
        时间格式20250331,20250630,20250930,20251230
        '''
        name='估值数据'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_balance_statement(self,date='2025-09-30'):
        '''
        资产负债
        date没有输入返回全部数据
        时间格式2025-03-31,2025-06-30,2025-09-30,2025-12-30
        '''
        name='资产负债'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_income_statement(self,date='2025-09-30'):
        '''
        利润
        date没有输入返回全部数据
        时间格式2025-03-31,2025-06-30,2025-09-30,2025-12-30
        '''
        name='利润'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_cashflow_statement(self,date='2017-09-30'):
        '''
        现金流表
        date没有输入返回全部数据
        时间格式2025-03-31,2025-06-30,2025-09-30,2025-12-30
        '''
        name='现金流表'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_growth_ability(self,date='2025-09-30'):
        '''
        成长能力
        date没有输入返回全部数据
        时间格式2025-03-31,2025-06-30,2025-09-30,2025-12-30
        '''
        name='成长能力'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_profit_ability(self,date='2025-09-30'):
        '''
        盈利能力
        date没有输入返回全部数据
        时间格式2025-03-31,2025-06-30,2025-09-30,2025-12-30
        '''
        name='盈利能力'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_eps(self,date='2025-09-30'):
        '''
        每股指标
        date没有输入返回全部数据
        时间格式2025-03-31,2025-06-30,2025-09-30,2025-12-30
        '''
        name='每股指标'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_operating_ability(self,date='2025-09-30'):
        '''
        营运能力
        date没有输入返回全部数据
        时间格式2025-03-31,2025-06-30,2025-09-30,2025-12-30
        '''
        name='营运能力'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def get_debt_paying_ability(self,date='2025-09-30'):
        '''
        偿债能力
        date没有输入返回全部数据
        时间格式2025-03-31,2025-06-30,2025-09-30,2025-12-30
        '''
        name='偿债能力'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    #其他特色数据*******************************
    def stock_market_activity_legu(self,date='20251205'):
        '''
        赚钱效应分析
        '''
        name='赚钱效应分析'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    
    def stock_zh_a_st_em(self):
        '''
        ST数据
        '''
        name='ST数据'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_tfp_em(self):
        '''
        停复牌信息
        '''
        name='停复牌信息'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_xgsr_ths(self):
        '''
        新股上市
        '''
        name='新股上市'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_account_statistics_em(self):
        '''
        股票账户统计月度
        '''
        name='股票账户统计月度'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_hot_follow_xq(self,date='20251205'):
        '''
        股票热度雪球
        '''
        name='股票热度雪球'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_hot_tweet_xq(self,date='20251205'):
        '''
        雪球讨论排行榜
        '''
        name='雪球讨论排行榜'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_hot_deal_xq(self,date='20251205'):
        '''
        雪球交易排行榜
        '''
        name='雪球交易排行榜'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_hot_rank_em(self,date='20251205'):
        '''
        东方财富人气榜A股
        '''
        name='东方财富人气榜A股'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_hot_up_em(self,date='20251205'):
        '''
        东方财富飙升榜A股
        '''
        name='东方财富飙升榜A股'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(date)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_info_a_code_name(self):
        '''
        股票列表A股
        '''
        name='股票列表A股'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_a_congestion_lg(self):
        '''
        大盘拥挤度
        '''
        name='大盘拥挤度'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_a_high_low_statistics(self):
        '''
        创新高和新低的股票数量
        '''
        name='创新高和新低的股票数量'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_a_below_net_asset_statistics(self):
        '''
        破净股统计
        '''
        name='破净股统计'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_margin_ratio_pa(self):
        '''
        标的证券名单及保证金比例
        '''
        name='标的证券名单及保证金比例'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_margin_account_info(self):
        '''
        两融账户信息
        '''
        name='两融账户信息'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_margin_sse(self):
        '''
        上海融资融券汇总
        '''
        name='上海融资融券汇总'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_margin_detail_sse(self):
        '''
        上海融资融券明细
        '''
        name='上海融资融券明细'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_margin_szse(self):
        '''
        深圳融资融券汇总
        '''
        name='深圳融资融券汇总'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_margin_detail_szse(self):
        '''
        深圳融资融券明细
        '''
        name='深圳融资融券明细'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df
    def stock_margin_underlying_info_szse(self):
        '''
        深圳标的证券信息
        '''
        name='深圳标的证券信息'
        file_path= '/data/{}/'.format(name)
        file_name='{}'.format(name)
        url='{}:{}/{}?'.format(self.url,self.port,'get_user_base_data')
        params={
            'password':self.password,
            'file_path':file_path,
            "file_name":file_name
        }
        response = requests.get(
            url=url,
            params=params,
            timeout=300
        )
        res=response.json()
        df=self.data_to_pandas(res)
        return df

if __name__=='__main__':
    '''
    西蒙斯金融量化交易数据库3
    作者:索普量化
    微信:xms_quant
    '''
    client=xms_quant_trader_data(
        #url='http://127.0.0.1'
        
       )
    df=client.stock_market_activity_legu()
    print(df)
    
    
    
    