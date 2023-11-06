import numpy as np


def first():
    # 1 data
    receipts = [739, 642, 125, 984, 490, 712, 635, 643, 189, 370, 752, 357, 384, 756, 171, 153, 155, 695, 831, 618, 898,
                115, 624, 592, 684, 799, 461, 96]
    # 2
    print("-" * 30)
    days_receipts = np.array(receipts).reshape(-1, 7)
    print("Days receipts: ", days_receipts)

    # 3
    print("-" * 30)
    total_receipts = np.sum(days_receipts)
    print("Total receipts: ", total_receipts)

    # 4
    print("-" * 30)
    total_week_receipts = np.sum(days_receipts, axis=1)
    print("Total week receipts: ", total_week_receipts)

    # 5
    print("-" * 30)
    print("Equal: ", total_week_receipts == total_receipts)

    # 6
    print("-" * 30)
    average_day_receipts = np.mean(days_receipts, axis=0)
    print("Average day receipts: ", average_day_receipts)

    # 7
    print("-" * 30)
    max_average_day_receipts = np.max(average_day_receipts)
    print("Max average day receipts: ", max_average_day_receipts)

    # 8
    print("-" * 30)
    days_receipts[:, 0] = 0
    print("Days receipts: ", days_receipts)

    # 9
    print("-" * 30)
    weekend_receipts = np.sum(days_receipts[:, 5:7], axis=1)
    print("Weekend receipts: ", weekend_receipts)

    # 9
    print("-" * 30)
    days_receipts = days_receipts.transpose()
    print("Days receipts: ", days_receipts)
