import torch.utils.data

# Todo: disentangle data-related parameters from model options

def CreateDataLoader(opt, split='test'):
    # loader = CustomDataLoader()
    # loader.initialize(opt)
    # return loader

    dataset = CreateDataset(opt, split)
    shuffle = (split == 'train' and opt.is_train)
    drop_last = opt.is_train
    dataloader = torch.utils.data.DataLoader(
        dataset = dataset, 
        batch_size = opt.batch_size,
        shuffle = shuffle, 
        num_workers = 8,
        drop_last = drop_last,
        pin_memory = False)
    return dataloader

def CreateDataset(opt, split):
    dataset = None
    if opt.dataset_type == 'flow':
        from data.flow_dataset import FlowDataset as DatasetClass
    elif opt.dataset_type == 'pose_transfer':
        from data.pose_transfer_dataset import PoseTransferDataset as DatasetClass
    else:
        raise ValueError('Dataset mode [%s] not recognized.' % opt.dataset_type)
    
    dataset = DatasetClass()
    dataset.initialize(opt, split)
    print('Dataset [%s] was created (size: %d).' % (dataset.name(), len(dataset)))

    return dataset

