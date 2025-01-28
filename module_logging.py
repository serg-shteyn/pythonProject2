import logging

print('module - logging')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    logging.debug('debug')
    logging.info('i')
    logging.warning('warning')
    logging.error('error')
    logging.critical('crit')