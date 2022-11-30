#pragma once
#include "FImportedAssetData.generated.h"

UENUM(BlueprintType)
enum class EAssetImportTypeEnum : uint8 {
	Meshes,
	Sounds,
	Textures
};

USTRUCT(BlueprintType)
struct FImportedAssetData
{
	GENERATED_BODY()
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	FString AssetName;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	FString AssetPath;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	FString AssetDestination;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	FString AssetExtension;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	EAssetImportTypeEnum AssetType;
};

USTRUCT(BlueprintType)
struct FImportAssetStruct
{
	GENERATED_BODY()
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	FString AssetPath;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	bool ImportMeshes;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	bool ImportSounds;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	bool ImportTextures;
};
