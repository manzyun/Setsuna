import random
import time
from .. import conf as db
from .. import conf
from bson import objectid

# _LANG_LIST base is ISO 639-3
_LANG_LIST = {'aar', 'abk', 'ace', 'ach', 'ada', 'ady', 'afh', 'afr', 'ain',
            'aka', 'akk', 'ale', 'alt', 'amh', 'ang', 'anp', 'ara', 'arc', 'arg',
            'arn', 'arp', 'arw', 'asm', 'ast', 'ava', 'ave', 'awa', 'aym', 'aze',
            'bak', 'bal', 'bam', 'ban', 'bas', 'bej', 'bel', 'bem', 'ben', 'bho',
            'bik', 'bin', 'bis', 'bla', 'bod', 'bod', 'bos', 'bra', 'bre', 'bua',
            'bug', 'bul', 'byn', 'cad', 'car', 'cat', 'ceb', 'ces', 'ces', 'cha',
            'chb', 'che', 'chg', 'chk', 'chm', 'chn', 'cho', 'chp', 'chr', 'chu',
            'chv', 'chy', 'cop', 'cor', 'cos', 'cre', 'crh', 'csb', 'cym', 'cym',
            'dak', 'dan', 'dar', 'del', 'den', 'deu', 'deu', 'dgr', 'din', 'div',
            'doi', 'dsb', 'dua', 'dum', 'dyu', 'dzo', 'efi', 'egy', 'eka', 'ell',
            'ell', 'elx', 'eng', 'enm', 'epo', 'est', 'eus', 'eus', 'ewe', 'ewo',
            'fan', 'fao', 'fas', 'fas', 'fat', 'fij', 'fil', 'fin', 'fon', 'fra',
            'fra', 'frm', 'fro', 'frr', 'frs', 'fry', 'ful', 'fur', 'gaa', 'gay',
            'gba', 'gez', 'gil', 'gla', 'gle', 'glg', 'glv', 'gmh', 'goh', 'gon',
            'gor', 'got', 'grb', 'grc', 'grn', 'gsw', 'guj', 'gwi', 'hai', 'hat',
            'hau', 'haw', 'heb', 'her', 'hil', 'hin', 'hit', 'hmn', 'hmo', 'hrv',
            'hsb', 'hun', 'hup', 'hye', 'hye', 'iba', 'ibo', 'ido', 'iii', 'iku',
            'ile', 'ilo', 'ina', 'ind', 'inh', 'ipk', 'isl', 'isl', 'ita', 'jav', 
            'jbo', 'jpn', 'jpr', 'jrb', 'kaa', 'kab', 'kac', 'kal', 'kam', 'kan',
            'kas', 'kat', 'kat', 'kau', 'kaw', 'kaz', 'kbd', 'kha', 'khm', 'kho', 
            'kik', 'kin', 'kir', 'kmb', 'kok', 'kom', 'kon', 'kor', 'kos', 'kpe',
            'krc', 'krl', 'kru', 'kua', 'kum', 'kur', 'kut', 'lad', 'lah', 'lam',
            'lao', 'lat', 'lav', 'lez', 'lim', 'lin', 'lit', 'lol', 'loz', 'ltz',
            'lua', 'lub', 'lug', 'lui', 'lun', 'luo', 'lus', 'mad', 'mag', 'mah',
            'mai', 'mak', 'mal', 'man', 'mar', 'mas', 'mdf', 'mdr', 'men', 'mga',
            'mic', 'min', 'mis', 'mkd', 'mkd', 'mlg', 'mlt', 'mnc', 'mni', 'moh',
            'mon', 'mos', 'mri', 'mri', 'msa', 'msa', 'mul', 'mus', 'mwl', 'mwr',
            'mya', 'mya', 'myv', 'nap', 'nau', 'nav', 'nbl', 'nde', 'ndo', 'nds',
            'nep', 'new', 'nia', 'niu', 'nld', 'nld', 'nno', 'nob', 'nog', 'non',
            'nor', 'nqo', 'nso', 'nwc', 'nya', 'nym', 'nyn', 'nyo', 'nzi', 'oci',
            'oji', 'ori', 'orm', 'osa', 'oss', 'ota', 'pag', 'pal', 'pam', 'pan',
            'pap', 'pau', 'peo', 'phn', 'pli', 'pol', 'pon', 'por', 'pro', 'pus',
            'qaa-qtz', 'que', 'raj', 'rap', 'rar', 'roh', 'rom', 'ron', 'ron', 'run',
            'rup', 'rus', 'sad', 'sag', 'sah', 'sam', 'san', 'sas', 'sat', 'scn',
            'sco', 'sel', 'sga', 'shn', 'sid', 'sin', 'slk', 'slk', 'slv', 'sma',
            'sme', 'smj', 'smn', 'smo', 'sms', 'sna', 'snd', 'snk', 'sog', 'som',
            'sot', 'spa', 'sqi', 'sqi', 'srd', 'srn', 'srp', 'srr', 'ssw', 'suk',
            'sun', 'sus', 'sux', 'swa', 'swe', 'syc', 'syr', 'tah', 'tam', 'tat',
            'tel', 'tem', 'ter', 'tet', 'tgk', 'tgl', 'tha', 'tig', 'tir', 'tiv',
            'tkl', 'tlh', 'tli', 'tmh', 'tog', 'ton', 'tpi', 'tsi', 'tsn', 'tso',
            'tuk', 'tum', 'tur', 'tvl', 'twi', 'tyv', 'udm', 'uga', 'uig', 'ukr',
            'umb', 'und', 'urd', 'uzb', 'vai', 'ven', 'vie', 'vol', 'vot', 'wal',
            'war', 'was', 'wln', 'wol', 'xal', 'xho', 'yao', 'yap', 'yid', 'yor',
            'zap', 'zbl', 'zen', 'zha', 'zho', 'zho', 'zul', 'zun', 'zxx', 'zza',
}

class Post:
    '''
    Base post class.  

    uid -- identity key from DB.  
    content -- Post content.  
    limit -- Delete time. Record style is Unix time.  
    password -- Password for manually delete.
    lang -- Language code by ISO 639-3.  
    '''
    def __init__(self, content: str, password: str, lang: str):
        '''
        Make post.  

        content -- Post content.  
        limit -- Delete time. Record style is Unix time.  
        password -- Password for manually delete.  
        lang -- Language code by ISO 639-3.  
        '''
        self.content = content
        self.limit = int(time.time()) + 3600 * conf.life
        self.password = self.make_password() if '' else password
        self.lang = lang if not lang in _LANG_LIST else 'und'


    def post_contribution(self) -> str:
        '''
        Post contribution.

        return -- identity key from DB
        '''
        result = db.posts.insert_one({'content': self.content,
                                'limit': self.limit,
                                'password': self.password,
                                'lang': self.lang
                                })
        self.id = result.inserted_id
        return self.id


    def apothanasia(self):
        '''
        Contribution prolonging life.  

        return -- new delete limit time.
        '''
        self.limit = self.limit + 3600
        db.posts.update_one({'_id': objectid.ObjectId(self.id)},
                            {'$set': {'limit': self.limit}})


    def get_post(self, uid: str):
        '''
        Get contribution from DB.  

        uid -- identity ID
        '''
        re = db.posts.find_one({'_id': objectid.ObjectId(uid)})
        if 'link' in re:
            raise TypeError(repr(re) + ' is not nomal contributon.')
        self.id = re['_id']
        self.content = re['content']
        self.limit = re['time']
        self.password = re['password']
        self.lang = re['lang']


    def password_checker(self, password: str):
        '''
        Password checker
        
        password -- Sample password
        '''
        if password == self.password:
            return True
        else:
            return False


    def delete_post(self):
        '''
        Delete Contribution from DB.  
        '''
        db.posts.delete_one({'_id': objectid.ObjectId(self.id)})


    def make_password(length=4) -> str:
        '''
        Make password

        length -- Make password digit.  
        return -- Password.  
        '''

        # Make font map
        alphabets = []
        codes = (('a', 'z'), ('A', 'Z'), ('0', '9'))
        for r in codes:
            chars = map(chr, range(ord(r[0]), ord(r[1]) + 1))
            alphabets.extend(chars)

            password = [random.choice(alphabets) for _ in range(length)]
            password = ''.join(password)

            return password
