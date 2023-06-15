"""Copyright (c) Facebook, Inc. and its affiliates.
All rights reserved.

This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

from .ResNextFeature import *
from ...utils import init_weights
from os import path
        
def create_model(logger, use_selfatt=False, use_fc=False, dropout=None, stage1_weights=False, dataset=None, log_dir=None, test=False, *args):
    
    logger.info('Loading Scratch ResNext 50 Feature Model.')
    resnext = ResNext(Bottleneck, [3, 4, 6, 3], use_modulatedatt=use_selfatt, use_fc=use_fc, dropout=None,
                       groups=32, width_per_group=4, use_glore=False, use_gem=False)

    if not test:
        if stage1_weights:
            assert(dataset)
            logger.info('Loading %s Stage 1 ResNext 50 Weights.' % dataset)
            if log_dir is not None:
                weight_dir = path.join('/'.join(log_dir.split('/')[:-1]), 'stage1')
            else:
                weight_dir = './logs/%s/stage1' % dataset
            logger.info('==> Loading weights from %s' % weight_dir)
            resnext = init_weights(model=resnext,
                                    weights_path=path.join(weight_dir, 'final_model_checkpoint.pth'))
        else:
            logger.info('No Pretrained Weights For Feature Model.')

    return resnext